PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE doorTable(name TEXT DEFAULT 'DingLing',tdatetime DATETIME DEFAULT (datetime('now','localtime')),door_status TEXT NOT NULL);

INSERT INTO doorTable VALUES('DingLing',datetime('now','localtime','-3 hours'),'opened');
INSERT INTO doorTable VALUES('DingLing',datetime('now','localtime','-2 hours'),'closed');
INSERT INTO doorTable VALUES('DingLing',datetime('now','localtime','-1 hours'),'opened');

COMMIT;

