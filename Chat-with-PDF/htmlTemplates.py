css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="data:image/png;base64,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" alt="Bot Image" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,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" alt="Bot Image" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''