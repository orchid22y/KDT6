/*	*****************************************************************************
 * 	제어문 - for 반복문
 *	*****************************************************************************/
public class EX_Loop {
	public static void main(String[] args) {
		// 여러개의 변수를 가지는 반복문
		for(int x=0,y=5;x<10 && y<8;x++,y++)	//변수가 여러개일때 타입이 1가지인 경우 타입 1번만 작성 가능
		{
			System.out.printf("%d *%d = %d %n", x, y, x*y);
		}
		
		// 무한 반복문
//		for(int a=0; ; a++)
//			System.out.println(a);
//		
//		for(;;) System.out.println("Good");
		
//		for(int a=0; a<10;)
//			System.out.println(a);
		
	}
}
