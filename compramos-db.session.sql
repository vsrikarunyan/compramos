
/*  For performing a thorough database cleaning of the shopping_list app, run the following SQL commands in the database console:

DELETE FROM django_migrations WHERE app='shopping_list';
DELETE FROM django_content_type WHERE app_label='shopping_list';
DELETE FROM django_admin_log WHERE content_type_id IN (SELECT id FROM django_content_type WHERE app_label='shopping_list');
DELETE FROM django_content_type WHERE app_label='shopping_list';
*/


-- DELETE FROM django_migrations WHERE app='shopping_list';

-- IMPORTANT --
-- NEVER run the query using the Run Menu; always use the Command Pallate (Ctrl+Shift+P) and select "SQLTools: Run Query"
-- IMPORTANT --

SELECT * FROM shopping_list_shoppinglist_members;

SELECT * FROM shopping_list_shoppinglist;

SELECT * FROM auth_user;