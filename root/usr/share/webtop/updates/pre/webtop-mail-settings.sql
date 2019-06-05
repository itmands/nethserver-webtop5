-- ---------------------------------------------------
-- Set Mail grid view to columns, if setting not exist
-- ---------------------------------------------------
INSERT INTO "core"."settings" (service_id, key, value) SELECT 'com.sonicle.webtop.mail', 'default.viewmode', 'columns' WHERE NOT EXISTS (SELECT value from "core"."settings" WHERE key = 'default.viewmode' and service_id = 'com.sonicle.webtop.mail');

-- -------------------------------------------------------
-- Set Mail compact toolbar to false, if setting not exist
-- -------------------------------------------------------
INSERT INTO "core"."settings" ("service_id", "key", "value") SELECT 'com.sonicle.webtop.mail', 'toolbar.compact', 'false'  WHERE NOT EXISTS (SELECT value from "core"."settings" WHERE key = 'toolbar.compact' and service_id = 'com.sonicle.webtop.mail');
