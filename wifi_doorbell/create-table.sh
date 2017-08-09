#!/bin/sh

rm -f dingling.db

echo start create database and table

sqlite3 dingling.db < insert.sql

echo create database and table finishend
