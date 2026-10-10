import pygame


class StoryDirector:
    def __init__(self):
        self.timeline = []
        self.current_script = 0
        
        self.start_time = 0
        self.end_time = 0

    def add_script(self, type, actor, target, time=0):
        self.timeline.append(
            {"type": type, "actor": actor, "target": target, "time": time}
        )
        
    def play(self):
        if self.current_script >= len(self.timeline):
            self.current_script = 0
            
            return False
        
        if self.timeline[self.current_script]:
            current_action = self.timeline[self.current_script]
            
            if current_action['type'] == 'teleport':
                current_action['actor'].teleport(current_action['target'])
                
            self.current_script += 1
