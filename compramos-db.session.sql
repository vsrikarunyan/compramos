
/*  For performing a thorough database cleaning of the shopping_list app, run the following SQL commands in the database console:

DELETE FROM django_migrations WHERE app='shopping_list';
DELETE FROM django_content_type WHERE app_label='shopping_list';
DELETE FROM django_admin_log WHERE content_type_id IN (SELECT id FROM django_content_type WHERE app_label='shopping_list');
DELETE FROM django_content_type WHERE app_label='shopping_list';
*/


DELETE FROM django_migrations WHERE app='shopping_list';

DROP TABLE shopping_list_shoppinglist;