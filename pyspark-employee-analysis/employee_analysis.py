from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# Create Spark session
spark = SparkSession.builder \
    .appName("EmployeeDataAnalysis") \
    .getOrCreate()

# Read employee CSV file
df = spark.read.csv(
    "data/employees.csv",
    header=True,
    inferSchema=True
)

# Display employee records
print("Employee Data:")
df.show()

# Filter employees with salary above 40000
print("Employees earning above 40000:")
df.filter(df.salary > 40000).show()

# Average salary by department
print("Average Salary by Department:")
df.groupBy("department") \
    .agg(avg("salary").alias("average_salary")) \
    .show()

# Employee count by department
print("Employee Count by Department:")
df.groupBy("department") \
    .agg(count("*").alias("employee_count")) \
    .show()

spark.stop()
