const Discord = require("discord.js");
const client = new Discord.Client();
const Bot_config = require('./config.json');
client.on("ready", () => {
  console.log("I am ready!");
});

client.on("message", (message) => {
  if (message.content.startsWith("ping")) {
    message.channel.send("pong!");
  } else

  if (message.content.startsWith("foo")) {
      message.channel.send("bar");
  }
});

client.login(Bot_config.token);