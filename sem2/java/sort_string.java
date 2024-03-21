public class sort_string {
	public static void main(String []args){
        String temp;
        int i,j;
        String str[] = new String[5];
        str[0] = "Reshma";
        str[1] = "Arya";
        str[2] = "Shahana";
        str[3] = "Ganga";
        str[4] = "Anoop";
         System.out.println("The strings before sorting:");
        for(i=0;i<5;i++)
         {
             System.out.println(str[i]);
         }
        
        for (i=0; i<5; i++)
          {
              for(j=i+1;j<5;j++)
                {
                    if((str[i].compareTo(str[j]))>0)
                      {
                          temp=str[i];
                          str[i]=str[j];
                          str[j]=temp;
                      }
                }
              
          }
        System.out.println("\nThe strings after sorting:");
        for(i=0;i<5;i++)
         {
             System.out.println(str[i]);
         }
	}
}
