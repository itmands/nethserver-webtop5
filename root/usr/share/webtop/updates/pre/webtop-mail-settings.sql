-- ---------------------------------------------------
-- Set Mail grid view to columns, if setting not exist
-- ---------------------------------------------------
INSERT INTO "core"."settings" (service_id, key, value) SELECT 'com.sonicle.webtop.mail', 'default.viewmode', 'columns' WHERE NOT EXISTS (SELECT value from "core"."settings" WHERE key = 'default.viewmode' and service_id = 'com.sonicle.webtop.mail');
