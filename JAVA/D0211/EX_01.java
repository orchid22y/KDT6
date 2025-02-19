/* ***********************************************************************************************
 * 데이터 타입별 초기화 값
 * - 지역 변수 즉, 메서드 안에 있는 변수는 반드시 초기화 해야 함!
 * 
 * ********************************************************************************************** */
public class EX_01 {

	public static void main(String[] args) {
		// 타입별 변수 선언 및 초기화
		byte num1 = 0;			// 1바이트 메모리 1칸
		short num2 = 0;			// 2바이트 메모리 2칸
		int num3 = 0;			// 4바이트 메모리 4칸
		long num4 = 0;			// 8바이트 메모리 8칸
		
		float fnum1 = 0.0F;		// 4바이트 메모리 4칸 , F(f) 대소문자 상관 X, double과 구분하기 위해 f 표시 함.
		double fnum2 = 0.0;		// 8바이트 메모리 8칸, 실수는 기본 double
		
		boolean bOK =true;		// 1바이트 메모리 1칸, true 또는 false로 초기화, 0 사용 불가
		
		char cdata = 0;			// 2바이트 메모리 2칸, 내부적으로 유니코드 사용, empty string 없음
		String sdata = null ;	// 4바이트 메모리 4칸, 문자열 데이터 주소를 힙에 저장하기 때문에 0으로 초기화 불가
		
		
		
		
		
		
	}

}
