from playwright.sync_api import sync_playwright
from contexto import crear_contexto
from simulacion import human_like_mouse_move, human_like_scroll
import logging
from rich import print
import pandas as pd
from itertools import zip_longest
from urllib.parse import urljoin

# Configuración inicial
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

def bloquear_imagenes(route):
    if route.request.resource_type == "image":
        route.abort()
    else:
        route.continue_()


def main():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        contexto = crear_contexto(navegador)
        pagina = contexto.new_page()
        
        datos = [] # Lista para almacenar los datos extraidos

        # Bloqueo de imágenes para acelerar carga
        pagina.route("**/*", bloquear_imagenes)

        logging.info("Visitando BBC")
        try:
            pagina.goto("https://www.bbc.com/culture", wait_until="domcontentloaded", timeout=100000)
        except Exception as e:
            logging.error(f"Error al entrar en BBC: {e}")
            return  # Salir si no carga
        
        

        # Esperar a que aparezca el elemento
        try:
            pagina.wait_for_selector('h2[data-testid="card-headline"]', timeout=5000)
            titular = [el.text_content() for el in pagina.query_selector_all('h2[data-testid="card-headline"]')]
            logging.info("Titulares extraidos correctamente")
        except Exception as e:
            logging.error(f"Error al extraer los titulares: {e}")
            
        try:
            descripcion = [el.text_content().strip() for el in pagina.query_selector_all('p[data-testid="card-description"]')]
            logging.info("Descripciones extraidas correctamente")
        except Exception as e:
            logging.error(f"Error al extraer la descripciones: {e}")
                
        try:
            urls = [
                el.query_selector("a").get_attribute("href")
                for el in pagina.query_selector_all('div[data-testid="anchor-inner-wrapper"]')
            ]
        except Exception as e:
            logging.error(f"Error al extraer las urls: {e}")
            urls = []  # para evitar NameError más adelante

        # Filtrar solo las URLs que necesitas
        url_base = "https://www.bbc.com"
        urls_filtradas = []

        for u in urls:
            if u is None:
                continue  # Evitar errores si el href está vacío

            abs_url = urljoin(url_base, u)

            if (
                "/article/" in abs_url or "/news/articles/" in abs_url
            ) and not any(x in abs_url for x in ["privacy", "terms", "cookies", "contact", "help", "about"]):
                urls_filtradas.append(abs_url)
                
        logging.info("Urls extraidas correctamente")
                
        for title,description,url in zip_longest(titular,descripcion,urls_filtradas,fillvalue=None):
            datos.append({"titulo" : title,"descripcion":description,"urls":url})
            
        if datos:
            df = pd.DataFrame(datos)
            df.to_csv("noticias_bbc.csv", index=False)
            logging.info("✅ Datos guardados correctamente en noticias_bbc.csv")
        else:
            logging.warning("⚠️ No se extrajo ningún dato.")

                
                    
 
main()       
"""
datos = main()
for dato in datos:
    print(dato)"""
