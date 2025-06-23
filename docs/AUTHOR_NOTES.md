
*note 1*
I've already done a ton of setup at this point getting the project going and chatGPT understanding what I want.  Because of this you are going to see some repeat commit messages and such.   I wish I could show all of the "sidebar" conversations as I tell it how to act, but it will break it's little brain.

*note 2*
After prompt 7, I told CGPT to include the original text of my prompts along with the "instructions" which are an interpretation of the original prompt.

*note 3*
After prompt 10, the chat started to get slow and stupid. I just spent a bunch of time creating the transition process between chats and added an index now that I have things checked into github

*note 4*
this no editing my hand thing may have to fall by the wayside for markdown files which ChatGPT 4-o seems to have a particularly hard time with. My new chat window has already filled up its context window and is getting stupid and slow.  I'll have to transfer with the next commit.  I've been unfair.   I'm exhausted and was praising the wrong formats for markdown.  I finally got it right and CGP picked it up even though the context window is full.

*note 5*
I just had to create commit 0013 with the debug info.  I had already checked in the fixes and changes.  I'll try and append the changes, but I need to remember not to work on so little sleep.  I'll try to fix things so the index isn't all messed up.  Hopefully I can do it without touching the code.

*note 6*
It took me way too long to come up to speed with the process.  I need to figure out a way speed up coming back after a few days, weeks.   One thing that was a pain was finding the correct chat.  I guess I could delete the old ones...   Also just tried to create a patch and 4o is shit at creating patch files.  I'll see what happens under 4.1

*note 7* 
switching to 4.1 is interesting.  The code is wayyyyy better, but the ability to follow instructions is pretty bad.  It made unasked for improvements, but they were cool.  Getting it to follow my output formats was difficult.   I wish I could use 4.1 for code and 4o for the rest.

*note 8*
After the last refactor I'm going to rethink the project structure PROMTS.md and CHAT_LOG.md seem redundant.  Along with a CHAT_LOG.md will probably be replaced with the devlog

*note 9*
So, 4.1 does stealth refactors which can seriously mess things up.  I had to add explict instructions to not refactor unless asked to, then it went too far and couldn't actually make necessary changes because they were a refactor.   So I loosened it a bit.   I may have to find a tight definition of refacor to include in the boot prompt.

*note 10*
Just had the LLM optamize my chat boot, it suggested adding a strict and explicit policy around getting everyting in a single markdown code block.   We'll see how well it works, it's been a pain in the ass and I'm tired of yelling at it whih seems to work.
