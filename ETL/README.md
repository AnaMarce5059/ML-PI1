# ETL - Extracción, Transformación y Carga de Datos
## Descripción: Esta carpeta contiene el script para realizar la limpieza y transformación de los datos de Mouvies y Credits. 
El proceso de ETL incluye las siguientes transformaciones:
**Desanidar columnas anidadas**:
1. Extraer información útil de columnas que contienen diccionarios o listas de diccionarios (como `belongs_to_collection`, `genres`, etc.). 
2. **Lidiar con valores nulos**: Rellenar los valores nulos en las columnas `revenue` y `budget` con `0`. 
3. **Formatear fechas**: Eliminar filas con fechas nulas en `release_date` y convertir las fechas al formato `AAAA-mm-dd`. 
4. **Generar nuevas columnas**: Crear las columnas `release_year` y `return` (retorno de inversión). 
5. **Eliminar columnas innecesarias**: Eliminar columnas no requeridas como `video`, `imdb_id`, etc.
## Archivos - **etl.py**: 
Este script realiza todas las transformaciones mencionadas anteriormente. - **movies_cleaned.csv**: Archivo CSV que contiene los datos de las películas después del proceso de limpieza. –
