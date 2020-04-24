/*
Wolven kit - 0.3.1.0
14/02/2020
*/

exec function printString()
{
	thePlayer.DisplayHudMessage("testing");
}

exec function writeCurrentQuest()
{
	var currentQuest : CJournalQuest;
	currentQuest = theGame.GetJournalManager().GetTrackedQuest();
	
	LogChannel('ChatMod',"current_quest:"+GetLocStringById(currentQuest.GetTitleStringId()));
}

exec function writeCurrentObjective()
{
	var currentObjective : CJournalQuestObjective;
	currentObjective = theGame.GetJournalManager().GetHighlightedObjective();

	LogChannel('ChatMod',"current_objective:"+GetLocStringById(currentObjective.GetTitleStringId()));
}

exec function writeMonsters()
{
	var enemies_list : array<CActor>;
	var actor : CActor;
	var response : string;
	var i : int;

	thePlayer.GetEnemiesInRange(enemies_list);
	
	for(i = 0; i <  enemies_list.Size(); i+=1)
	{	
		actor = enemies_list[i];
		if(actor.IsMonster())
		{
			response += actor.GetDisplayName()+","+actor.GetLevel() + ";";
		}
		
	}
	
	LogChannel('ChatMod',"monsters:"+ response);
}

exec function writeGeraltHealth()
{
	LogChannel('ChatMod',"geralt_health:"+thePlayer.GetLevel());
}