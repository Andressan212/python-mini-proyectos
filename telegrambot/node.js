const TelegramBot = require('node-telegram-bot-api');
const token = 'TU_TOKEN_AQUI';
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, "¡Hola! Soy tu bot en Node.js.");
});
