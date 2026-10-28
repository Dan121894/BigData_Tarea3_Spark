from pyspark.sql import SparkSession

# Crear sesión de Spark
spark = SparkSession.builder.appName("AnalisisBatchUNAD").getOrCreate()

# Crear un DataFrame simple simulado de datos
data = [
    ("Sensor_1", 25.5, 60.0),
    ("Sensor_2", 28.1, 55.2),
    ("Sensor_3", 22.4, 65.8),
    ("Sensor_1", 26.0, 58.5)
]
columns = ["sensor_id", "temperatura", "humedad"]

df = spark.createDataFrame(data, schema=columns)

print("--- VISTA DEL DATAFRAME ---")
df.show()

print("--- PROMEDIO DE TEMPERATURA POR SENSOR ---")
df.groupBy("sensor_id").avg("temperatura").show()