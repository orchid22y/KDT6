/*	************************************************************************************
 *  배열(Array) 선언 및 활용
 *  	: 동일한 데이터 타입의 데이터를 연속된 메모리 공간에 저장하는 것
 *  	: 배열 원소 활용
 *	************************************************************************************/
import java.util.Scanner;

public class EX_Array04 {

	public static void main(String[] args) {
		// 사용자로부터 점수를 입력 받아서 배열에 저장 후 합계와 평균을 출력 하기
		
		Scanner keyboard = new Scanner(System.in);
		System.out.print("입력 받을 과목 수를 입력하세요 :  ");
		int num = keyboard.nextInt();
		
		//배열 선언
		int[] jumsuArray = new int[num];
		
		int total = 0;
		float avg = 0.f;
		
		//배열 초기화 및 합계,평균 계산
		for(int idx=0;idx<num;idx++)
		{
			System.out.print("점수 입력: ");
			jumsuArray[idx]= keyboard.nextInt();
			
			total+=jumsuArray[idx];
			avg= total/(float)(idx+1);
		}
		
		System.out.println("점수 입력이 끝났습니다.\n");
		System.out.println("합계 : "+ total);
		System.out.println("평균 : "+ avg);
		
		/*
		 * >출력>>
		 * 입력 받을 과목 수를 입력하세요 :  5
		   점수 입력: 21
		   점수 입력: 28
		   점수 입력: 60
		   점수 입력: 57
		   점수 입력: 37
		   점수 입력이 끝났습니다.

		   합계 : 203
		   평균 : 40.6
		 */
				
		//입력 닫기
		keyboard.close();
		
		
	}

}
