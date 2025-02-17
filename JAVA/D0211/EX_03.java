/* **************************************************************************************************
 * 리터럴 문자
 * - 숫자 사이에 '_' 삽입 => 사람을 위한 가독성
 * - 바이트 코드 변환 시엔 무시 됨
 * ************************************************************************************************* */


public class EX_03 {

	public static void main(String[] args) {
		// 숫자와 '_'
		
		int jumin=2010_1212;
		int num = 0b010101_00011;
		int age = 2___5;
		//int jumsu=100_;			//ERROR : 숫자 사이에서만 _ 가능함!
		long maxvalue=100_0L;
		//long maxvalue=100_0_L;	//ERROR : L,F,D 같은 데이터 타입 식별 문자 앞에는 불가
		//int jumsu=0b_01010;		//ERROR : 0, 0b, 0x 사이, 뒤에 불가
		//'_'는 앞뒤로 숫자가 있을 경우에만 사용 가능
		float avg=9_8.8_8f;
		//float avg=9_8.88_f; 		//ERROR : 식별자 앞에 사용x
		//float avg=98_.88f;		//ERROR  : 소수점은 숫자x, 앞뒤로 사용X
		
		
		
		//화면 출력
		System.out.println(jumin);
		System.out.println(num);
		System.out.println(age);
		

	}

}
