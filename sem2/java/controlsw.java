class controlsw
{
public static void main(String args[])
{
int ch=12;
String season;
switch(ch)
{
case 1:
case 2:
case 12:
     season="winter";
     break;
case 3:
case 4:
case 5:
     season="spring";
     break;
case 6:
case 7:
case 8:
     season="summer";
     break;
default:
      season="bogus month";
}
System.out.println("april is in the" + season +".");
}
}
