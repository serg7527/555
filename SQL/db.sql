CREATE OR REPLACE FUNCTION set_updated()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated = now();
    RETURN NEW;
END;
$$ language 'plpgsql';


CREATE SEQUENCE users_seq;

CREATE TABLE IF NOT EXISTS users (
    id bigint PRIMARY KEY DEFAULT nextval('users_seq'),
    username varchar(32) UNIQUE NOT NULL,
    email varchar(256) UNIQUE NOT NULL,
    password text NOT NULL,
    info json NOT NULL, 
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE SEQUENCE costomers_seq;

CREATE TABLE IF NOT EXISTS costomers (
    id bigint PRIMARY KEY DEFAULT nextval('users_seq'),
    user_id bigint UNIQUE NOT NULL,
    address text NOT NULL,
    info json,
    --created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    --updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    FOREIGN KEY (user_id) REFERENCES users(id)
);


CREATE SEQUENCE staffs_seq;

CREATE TABLE IF NOT EXISTS staffs (
    id bigint PRIMARY KEY DEFAULT nextval('users_seq'),
    user_id bigint UNIQUE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    status varchar(1) NOT NULL,
    --permissions
    CONSTRAINT status_check CHECK (status IN ('A', 'M', 'C')),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


CREATE SEQUENCE dealers_seq;

CREATE TABLE IF NOT EXISTS dealers (
    id bigint PRIMARY KEY DEFAULT nextval('dealers_seq'),
    name varchar(20) NOT NULL,
    description text NOT NULL
);


CREATE SEQUENCE categories_seq;

CREATE TABLE  IF NOT EXISTS categories (
    id bigint PRIMARY KEY DEFAULT nextval('categories_seq'),
    name varchar(20) UNIQUE NOT NULL,
    is_root BOOLEAN DEFAULT FALSE,
    parentn_id bigint,
    description text NOT NULL,
    FOREIGN KEY (parentn_id) REFERENCES categories(id)
);


CREATE SEQUENCE sales_seq;

CREATE TABLE IF NOT EXISTS sales (
    id bigint PRIMARY KEY DEFAULT nextval('sales_seq'),
    discount decimal(3, 1),
    type varchar(5) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT FALSE
);


CREATE SEQUENCE batches_seq;

CREATE TABLE IF NOT EXISTS batches (
    id bigint PRIMARY KEY DEFAULT nextval('batches_seq'),
    sale_id bigint,
    dealer_id bigint NOT NULL,
    info json NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sale_id) REFERENCES sales(id),
    FOREIGN KEY (dealer_id) REFERENCES dealers(id)
);


CREATE SEQUENCE images_seq;

CREATE TABLE IF NOT EXISTS images (
    id bigint PRIMARY KEY DEFAULT nextval('images_seq'),
    path text NOT NULL UNIQUE
);


CREATE SEQUENCE items_seq;

CREATE TABLE IF NOT EXISTS items (
    id bigint PRIMARY KEY DEFAULT nextval('items_seq'),
    name varchar(50) NOT NULL,
    description text NOT NULL,
    cost decimal(10, 2),
    category_id bigint NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);


CREATE TABLE IF NOT EXISTS images_items (
    image_id bigint NOT NULL,
    item_id bigint NOT NULL,
    FOREIGN KEY (image_id) REFERENCES images(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);
########

CREATE SEQUENCE backets_seq;

CREATE TABLE IF NOT EXISTS backets (
    id bigint PRIMARY KEY DEFAULT nextval('backets_seq'),
    opened BOOLEAN DEFAULT TRUE,
    customer_id bigint NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS backets_items (
    backet_id bigint NOT NULL,
    item_id bigint NOT NULL,
    FOREIGN KEY (backet_id) REFERENCES backets(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);


CREATE SEQUENCE orders_seq;

CREATE TABLE IF NOT EXISTS orders (
    id bigint PRIMARY KEY DEFAULT nextval('orders_seq'),
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status varchar(1) NOT NULL,
    address text,
    pay_info json,
    CONSTRAINT status_check CHECK (status IN ('N', 'P', 'S', ''))
);


CREATE TRIGGER users_updated BEFORE UPDATE
ON users FOR EACH ROW
EXECUTE FUNCTION set_updated();


CREATE TRIGGER batches_updated BEFORE UPDATE
ON batches FOR EACH ROW
EXECUTE FUNCTION set_updated();


CREATE TRIGGER backets_updated BEFORE UPDATE
ON backets FOR EACH ROW
EXECUTE FUNCTION set_updated();


CREATE TRIGGER orders_updated BEFORE UPDATE
ON orders FOR EACH ROW
EXECUTE FUNCTION set_updated();


