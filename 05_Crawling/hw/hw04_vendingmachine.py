class VendingMachineL:
    def __init__(self, input_dict):
        '''
        생성자
        :param input_dict : 초기 자판기 재료량 (dict형태)
        '''
        self.input_money=0
        self.inventory=input_dict

    
    def run(self):
        '''
        커피 자판기 동작 및 메뉴 호출 함수
        '''
        