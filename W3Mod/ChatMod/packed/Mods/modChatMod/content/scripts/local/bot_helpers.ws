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
	
	LogChannel('testmod',"current_quest:"+GetLocStringById(currentQuest.GetTitleStringId()));
}

exec function writeMonstersLevel()
{
	var monster_list : array<CActor>;
	var levels : string;
	var i : int;

	thePlayer.GetEnemiesInRange(monster_list);
	
	for(i = 0; i <  monster_list.Size(); i+=1)
	{
		levels += monster_list[i].GetLevel() + " ";
	}
	
	LogChannel('testmod', levels);
}

exec function writeGeraltHealth()
{
	LogChannel('testmod',"geralt_health:"+thePlayer.GetLevel());
}