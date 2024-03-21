class product
{
 int pcode;
 double price;
 String pname;
}
class getproduct{
public static void main(String args[]){
product p1=new product();
product p2=new product();
product p3=new product();
p1.price=1000;
p1.pcode=101;
p1.pname="shampoo";
p2.price=2000;
p2.pcode=102;
p2.pname="conditioner";
p3.price=100;
p3.pcode=103;
p3.pname="perfume";
if(p1.price<p2.price && p1.price<p3.price)
{
System.out.println("smallest price:" + p1.pcode);
System.out.println(p1.pname);
System.out.println(p1.price);
}
else if(p2.price<p1.price && p2.price<p3.price)
{
System.out.println("smallest price:" + p2.pcode);
System.out.println(p2.pname);
System.out.println(p2.price);
}
else{
System.out.println("smallest price:" + p3.pcode);
System.out.println(p3.pname);
System.out.println(p3.price);
}
}
}
