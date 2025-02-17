/*	******************************************************************************************
 * 	제어문 - for 반복문
 *	******************************************************************************************/
public class EX_FOR_03 {

	public static void main(String[] args) {
		// 아무것도 반복하지 않는 반복문
		
		System.out.println("START");
		for(long idx=0; idx<1000000000000000l;idx++);
		
		
		for(int idx=0; idx<1000;idx++) {};
		
		
		System.out.println("END");
		
//		// 무한 반복문 (ex_사용자가 멈출때 까지 반복해야 하는 경우)
//		v1]
//		for (;;)
//		{	
//			System.out.println("OK");
//		}
		
//		v2]
//		for (int idx=0;;idx++);		
		
	}

}
