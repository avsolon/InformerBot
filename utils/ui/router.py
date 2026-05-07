class UIRouter:

    def __init__(self):
        self.stack = []

    def push(self, screen: str):
        self.stack.append(screen)

    def pop(self):
        if len(self.stack) > 1:
            self.stack.pop()
        return self.current()

    def current(self):
        if not self.stack:
            return "home"
        return self.stack[-1]

    def reset(self):
        self.stack = ["home"]