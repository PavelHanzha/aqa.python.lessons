from faker import Faker

f = Faker()

create_products_table = """CREATE TABLE public."products" (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    price TEXT NOT NULL,
    description TEXT NOT NULL,
    category_id INT REFERENCES public."categories"(category_id) ON DELETE SET NULL
);"""

create_categories_table = """CREATE TABLE public."categories" (
    category_id SERIAL PRIMARY KEY,
    category_name TEXT NOT NULL UNIQUE
);"""

add_category1 = f"""INSERT INTO public."categories" (category_name)
                   VALUES ('{f.word()}')"""
add_category2 = f"""INSERT INTO public."categories" (category_name)
                   VALUES ('{f.word()}')"""
add_category3 = f"""INSERT INTO public."categories" (category_name)
                   VALUES ('{f.word()}')"""
add_category4 = f"""INSERT INTO public."categories" (category_name)
                   VALUES ('{f.word()}')"""


add_product1 = f"""INSERT INTO public."products" (product_name, price, description, category_id)
                   VALUES ('{f.word()}', '{f.pricetag()}', '{f.text()}', {f.random_int(min=1, max=4)})"""
add_product2 = f"""INSERT INTO public."products" (product_name, price, description, category_id)
                   VALUES ('{f.word()}', '{f.pricetag()}', '{f.text()}', {f.random_int(min=1, max=4)})"""
add_product3 = f"""INSERT INTO public."products" (product_name, price, description, category_id)
                   VALUES ('{f.word()}', '{f.pricetag()}', '{f.text()}', {f.random_int(min=1, max=4)})"""
add_product4 = f"""INSERT INTO public."products" (product_name, price, description, category_id)
                   VALUES ('{f.word()}', '{f.pricetag()}', '{f.text()}', {f.random_int(min=1, max=4)})"""
add_product5 = f"""INSERT INTO public."products" (product_name, price, description, category_id)
                   VALUES ('{f.word()}', '{f.pricetag()}', '{f.text()}', {f.random_int(min=1, max=4)})"""


join = """SELECT 
    p.product_name,
    p.price,
    p.description,
    c.category_name
FROM public."products" p JOIN public."categories" c ON p.category_id = c.category_id"""
# "products" p - тут "p" виступає псевдонімом для скорочення запросу і далі я просто використовую "р"
# замість "products"
