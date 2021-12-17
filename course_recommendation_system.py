
PageManager:
    
    HomePage:
    
<HomePage>:
    name:"homepage"
    home:home
    MDCard:
        size_hint: None, None
        size: 400, 500
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'
        
    
    MDLabel:
        id: home
        text: "Welcome to CS Course Recomendation App"
        font_size: 15
        halign: 'center'
        size_hint_y: None
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        height: self.texture_size[1]
        padding_y: 15
        
    
    MDLabel:
       id: CSU_Login
       text: "What is your interest?"
       font_size: 40
       halign: 'center'
       size_hint_y: None
       pos_hint: {"center_x": 0.5, "center_y": 0.7}
       height: self.texture_size[0]
       padding_y: 15

   MDTextFieldRound:
       id: user
       hint_text: "Like Aritficial Intelligence, Web Devlopment"
       size_hint_x: None
       width: 200
       font_size: 18
       pos_hint: {"center_x": 0.5, "center_y": 0.6}
        
  
              
    Image:
        source:'Images/Logo.png'
        size_hint_x: 0.2
        allow_stretch: True
        pos_hint: {"center_x": 0.1, "center_y": 0.9}