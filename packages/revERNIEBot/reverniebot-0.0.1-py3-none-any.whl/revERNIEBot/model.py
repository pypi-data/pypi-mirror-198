

class ChatBotModel:
    """机器人类模型"""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def list_history(self):
        """列出所有历史记录"""
        raise NotImplementedError

    def check_history(self, *args, **kwargs):
        """获取指定历史记录内容"""
        raise NotImplementedError
    
    def delete_history(self, *args, **kwargs):
        """删除指定历史记录"""
        raise NotImplementedError
    
    def new_session(self, *args, **kwargs):
        """创建新对话"""
        raise NotImplementedError

    def rename_session(self, *args, **kwargs):
        """重命名对话"""
        raise NotImplementedError

    def ask(self, *args, **kwargs):
        """提问"""
        raise NotImplementedError

    def reset(self, *args, **kwargs):
        """重置对话"""
        raise NotImplementedError
    
    def rollback(self, *args, **kwargs):
        """回滚对话"""
        raise NotImplementedError

