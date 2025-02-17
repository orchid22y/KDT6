/*	**********************************************************************************
 * 	제어문 - do ~ while 반복문
 * 		: 최소 1번은 실행되는 반복문
 *	**********************************************************************************/
public class EX_DoWhile_02 {

	public static void main(String[] args) {
		// 문자 타입과 연산
		char ch=0;	// 정수
		
		System.out.println(ch+1);		// 1
		System.out.println(ch+10);		// 10
		
		
		ch='A';		// 아스키코드값 48
		
		System.out.println(ch+1);								// 66
		System.out.printf("%d -> %c\n",ch+1,(char)(ch+1));		// 66 -> B
		
		System.out.println(ch+10);									// 75
		System.out.printf("%d -> %c\n",ch+10,(char)(ch+10));		// 75 -> K
		
		System.out.println('A'+'C');								//132
		System.out.println((char)('A'+'C'));						//
		
		
		System.out.println('\n');	
		// a ~ z 까지 출력
		do{ 
			System.out.println(ch);
			ch++;
		}while(ch<'a');

	}

}
