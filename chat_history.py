import datetime
import extra_streamlit_components as stx



class ChatHistory():

    def __init__(self):
        self.cookie_manager = stx.CookieManager()
        self.chatxy_history_list = self.cookie_manager.get(cookie = "chatxy_history_list")
        if self.chatxy_history_list is None:   
            self.chatxy_history_list = []

    def list_items(self):
        return self.chatxy_history_list

    def add_item(self, topic):
        self.chatxy_history_list.append({"topic": topic, "datetime": datetime.datetime.now().timestamp()})
        self.cookie_manager.set(cookie = "chatxy_history_list", val = self.chatxy_history_list)

    def get_item(self, id):
        return self.chatxy_history_list[id]

    def delete_items(self, ids):
        self.chatxy_history_list = list(filter(lambda x: self.chatxy_history_list.index(x) not in ids, self.chatxy_history_list))
        self.cookie_manager.set(cookie = "chatxy_history_list", val = self.chatxy_history_list)

    def delete_all(self):
        self.chatxy_history_list = []
        self.cookie_manager.delete(cookie = "chatxy_history_list")

 
if __name__ == '__main__':
    chat_history = ChatHistory()
    chat_history.addItem(topic = "a")
    chat_history.addItem(topic = "b")
    chat_history.addItem(topic = "c")
    print(chat_history.getItem(id=0))
    print(chat_history.listItems())
    chat_history.deleteItems(ids = [0, 2])
    print(chat_history.listItems())
