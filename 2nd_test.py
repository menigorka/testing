from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_category_pairs(products_df, categories_df):
    product_category_df = products_df.join(categories_df, products_df['product_id'] == categories_df['product_id'], 'left_outer') \
        .select(products_df['product_name'], categories_df['category_name'])

    products_without_categories_df = product_category_df.filter(col('category_name').isNull()) \
        .select(products_df['product_name']).distinct()

    return product_category_df, products_without_categories_df

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("ProductCategoryPairs") \
        .getOrCreate()

    products_data = [("product1", 1), ("product2", 2), ("product3", 3)]
    categories_data = [(1, "category1"), (2, "category2")]

    products_df = spark.createDataFrame(products_data, ["product_name", "product_id"])
    categories_df = spark.createDataFrame(categories_data, ["product_id", "category_name"])

    product_category_pairs, products_without_categories = get_product_category_pairs(products_df, categories_df)

    print("Product-Category pairs:")
    product_category_pairs.show()
    print("\nProducts without categories:")
    products_without_categories.show()

    spark.stop()
