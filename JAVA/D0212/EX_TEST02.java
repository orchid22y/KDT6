
public class EX_TEST02 {

	public static void main(String[] args) {
		// 구구단 출력 하기

		for(int num=0; num<20;num++)
		{
			for(int dan=2; dan<10;dan++) 
			{
				if (num<10 && dan<6) 
				{
				
					if(num==0)
						System.out.printf(" ----%d단---- \t", dan);
					else
						System.out.printf(" %d * %d = %d\t ", dan, num, dan*num);
					}
						
					
				{
					if (num>=10 && dan>5)
				{
					int num2 = (num-10);
					if(num2==0)
						System.out.printf(" ----%d단---- \t", dan);
					else
						System.out.printf(" %d * %d = %d\t ", dan, num2, dan*num2);
				}
				}
				}
			System.out.printf("%n");	
		}
		
		System.out.printf("%n%n%n");
		
		
		
		//ver2
		for(int num=1; num<90; num++)
		{
			if(num/9==0)
				System.out.printf("   [%d단]   %c", num%9+1, ((num%9+1)==5||(num%9+1)==9)?'\n':'\t');
			
			else if((num%9+1)!=1)
				System.out.printf(" %d * %d = %d %c", num%9+1, num/9,(num/9)*(num%9+1),((num%9+1)==5||(num%9+1)==9)?'\n':'\t');
		}
		
		
		
		
		
		
		
		
//		
//		// 마름모 출력하기
//		for(int l=0; l<5; l++)
//		{
//			for(int c=0; c<5; c++)
//			{
//				System.out.printf("l%d,c%d\t",l,c);
//			}
//		System.out.printf("%n");
//		}
//			
//		

	}

}




