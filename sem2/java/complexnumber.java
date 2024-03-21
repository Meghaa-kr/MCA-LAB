class complexnumber {

	int real, image;

	public complexnumber(int r, int i)
	{
		this.real = r;
		this.image = i;
	}

	public void showC()
	{
		System.out.print(this.real + " +i" + this.image);
	}
 v
	{

		ComplexNumber res = new ComplexNumber(0, 0);

		res.real = n1.real + n2.real;

		res.image = n1.image + n2.image;
		return res;
	}

	public static void main(String arg[])
	{

		ComplexNumber c1 = new ComplexNumber(4, 5);
		ComplexNumber c2 = new ComplexNumber(10, 5);

		System.out.print("first Complex number: ");
		c1.showC();
		
		System.out.print("\nSecond Complex number: ");
		c2.showC();

		ComplexNumber res = add(c1, c2);

		System.out.println("\nAddition is :");
		res.showC();
	}
}

