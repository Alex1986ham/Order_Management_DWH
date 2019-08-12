
create_table = ("""
CREATE TABLE public.ama_order_export25
(
    order_id varchar,
    order_item_id character varying COLLATE pg_catalog."default",
    purchase_date character varying COLLATE pg_catalog."default",
    payments_date character varying COLLATE pg_catalog."default",
    reporting_date character varying COLLATE pg_catalog."default",
    promise_date character varying COLLATE pg_catalog."default",
    days_past_promise character varying COLLATE pg_catalog."default",
    buyer_email character varying COLLATE pg_catalog."default",
    buyer_name character varying COLLATE pg_catalog."default",
    buyer_phone_number character varying COLLATE pg_catalog."default",
    sku character varying COLLATE pg_catalog."default",
    product_name character varying COLLATE pg_catalog."default",
    quantity_purchased character varying COLLATE pg_catalog."default",
    quantity_shipped character varying COLLATE pg_catalog."default",
    quantity_to_ship character varying COLLATE pg_catalog."default",
    ship_service_level character varying COLLATE pg_catalog."default",
    recipient_name character varying COLLwATE pg_catalog."default",
    ship_address_1 character varying COLLATE pg_catalog."default",
    ship_address_2 character varying COLLATE pg_catalog."default",
    ship_address_3 character varying COLLATE pg_catalog."default",
    ship_city character varying COLLATE pg_catalog."default",
    ship_state character varying COLLATE pg_catalog."default",
    ship_postal_code character varying COLLATE pg_catalog."default",
	ship_country  character varying COLLATE pg_catalog."default",
	sales_channel  character varying COLLATE pg_catalog."default",
	is_prime  character varying COLLATE pg_catalog."default",
	fulfilled_by  character varying COLLATE pg_catalog."default",
	shipment_status  character varying COLLATE pg_catalog."default"
)
""")
