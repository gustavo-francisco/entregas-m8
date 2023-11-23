import rclpy
from rclpy.node import Node
import re

class ChatbotNode(Node):
    def __init__(self):
        super().__init__('chatbot_node')

    def going(self, local):
        if local.lower() == "almox" or "almoxarifado" or "packaging":
            return f"Indo para o {local}!"
        
        
    def returning(self, local):
        if local.lower() == "almox" or "almoxarifado" or "packaging":
            return f"Retornando ao {local}!"
        
    
    intent_dict = {
        r"\b(?:[Vv][aá])\s(?:[Pp]a?r?[ao])\s(?:o?)\s?([Aa]lmox(?:arifado)?)":"go",
        r"\b(?:[Mm]e\s[Ll]eve|[Ll]eve(-)?me)\s(?:[Pp]a?r[oa]|ao)\s?(?:o?)\s([Aa]lmox(?:arifado)?)":"go",
        r"\b(?:[Vv][aá])\s(?:[Pp]a?r[oa]|ao)\s?(?:o?)\s([Pp]ackaging)":"go",
        r"\b(?:[Mm]e\s[Ll]eve|[Ll]eve(-)?me)\s(?:[Pp]a?r[oa]|ao)\s?(?:o?)\s([Pp]ackaging)":"go",
        r"\b(?:[Rr]etorne)\s(?:[Pp]a?r[ao]|ao)\s?(?:o?)\s([Aa]lmox(?:arifado)?)":"return",
        r"\b(?:[Rr]etorne)\s(?:[Pp]a?r?[oa]|ao)\s?(?:o?)\s([Pp]ackaging)":"return",
    }

    action_dict = {
        "go": going,
        "return": returning,
    }

    def chat_loop(self):
        while rclpy.ok():
            command = input("Digite a movimentação desejada: ")
            for key, value in self.intent_dict.items():
                pattern = re.compile(key)
                groups = pattern.findall(command)
                if groups:
                    print(f"{self.action_dict[value](self, groups[0])}", end=" ")
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

    
