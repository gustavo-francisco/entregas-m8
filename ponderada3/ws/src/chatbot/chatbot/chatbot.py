import rclpy
from rclpy.node import Node
import re

class ChatbotNode(Node):
    def __init__(self):
        super().__init__('chatbot_node')

    def go_almox(self):
        return "Indo para o almoxarifado!"
        
    def go_packaging(self):
        return "Indo para o setor Packaging!"
        
    def return_almox(self):
        return "Retornando ao almoxarifado!"
        
    def return_packaging(self):
        return "Retornando ao setor Packaging!"
    
    intent_dict = {
        r"\b([Vv][aá])\s(?:[Pp]a?r?[ao])\s(?:o?)\s?(?:[Aa]lmox(arifado)?)":"go_almox",
        r"\b([Mm]e\s[Ll]eve|[Ll]eve(-)?me)\s(?:[Pp]a?r[oa]|ao)\s?(?:o?)\s(?:[Aa]lmox(arifado)?)":"go_almox",
        r"\b([Vv][aá])\s(?:[Pp]a?r[oa]|ao)\s?(?:o?)\s(?:[Pp]ackaging)":"go_packaging",
        r"\b([Mm]e\s[Ll]eve|[Ll]eve(-)?me)\s(?:[Pp]a?r[oa]|ao)\s?(?:o?)\s(?:[Pp]ackaging)":"go_packaging",
        r"\b([Rr]etorne)\s(?:[Pp]a?r[ao]|ao)\s?(?:o?)\s(?:[Aa]lmox(arifado)?)":"return_almox",
        r"\b([Rr]etorne)\s(?:[Pp]a?r?[oa]|ao)\s?(?:o?)\s(?:[Pp]ackaging)":"return_packaging",
    }

    action_dict = {
        "go_almox": go_almox,
        "go_packaging": go_packaging,
        "return_almox": return_almox,
        "return_packaging": return_packaging
    }

    def chat_loop(self):
        while rclpy.ok():
            command = input("Digite a movimentação desejada: ")
            for key, value in self.intent_dict.items():
                pattern = re.compile(key)
                groups = pattern.findall(command)
                if groups:
                    print(f"{self.action_dict[value](groups[0])}", end=" ")
            print()


def main(args=None):
    rclpy.init(args=args)
    chatbot_node = ChatbotNode()
    chatbot_node.chat_loop()
    rclpy.spin(chatbot_node)
    chatbot_node.destroy_node()
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()

    
