class product
{
 int pcode;
 double price;
 char pname;
}
class getproduct{
public static void main(String args[]){
product p1=new product();
product p2=new product();
product p3=new product();
p1.price=1001;
p2.price=2000;
p3.price=1000;
if(p1.price<p2.price && p1.price<p3.price)
{
System.out.println("smallest price:" + p1.price);
}
else if(p2.price<p1.price && p2.price<p3.price)
{
System.out.println("smallest price:" + p2.price);
}
else{
System.out.println("smallest price:" + p3.price);
}
}
}
