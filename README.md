# fosdick_exporter
This provides API code to interact with tradegecko.

## Export file format
This script will provide a file in the following export format which was provided by fosdick:

For each order start the export of the tab seperated file in a for loop
|Field	|Description			|Size (max. # of char.)		|Type (N=Number, A=Text)	|Required	|Picture/Notes							|
|-------|-------------------------------|-------------------------------|-------------------------------|---------------|---------------------------------------------------------------|
|1	|Order Number			|25				|A				|Yes		|							   	|	
|2	|Bill To First Name		|11				|A				|Yes		|The first name and last name fields are a total of 22 characters combined---so the length of each can be adjusted as needed and as long as the total does not go past 22 they will not be truncated. |		
|3	|Bill To Last Name		|11				|A				|Yes		|								|
|4	|Bill to Address #1		|30				|A				|Yes		|								|
|5	|Bill to Address #2		|30				|A				|No		|								|
|6	|Bill To Address #3		|30				|A				|No		|								|
|7	|Bill To City			|13				|A				|Yes		|								|
|8	|Bill To State			|2				|A				|Yes		|								|
|9	|Bill To Zip Code		|11				|A/N				|Yes		|								|
|10	|Bill To Country		|35				|A				|No		|								|
|11	|Bill To Phone			|10				|N				|No		|								|
|12	|Credit Card Type		|1				|A				|YES		|POPULATE ALL WITH "Q"						|
|13	|Credit Card Number		|16				|N				|NO		|								|
|14	|Credit Card Expiration		|6				|N				|NO		|								|
|15	|Authorization Code		|6				|N				|NO		|								|
|16	|Authorization Date		|8				|N				|NO		|								|
|17	|Source Code 			|5				|A/N				|No		|Should be left blank unless directed otherwise.		|
|17	|Order Type			|5				|A				|Yes		|PHONE or WEB							|
|17	|Media Code			|20				|A/N				|No		|Provided by client 						|
|17	|Opt in Flag			|1				|Y				|No		|Y = Remove from mailing list, *BLANK* = Leave on mailing list	|
|18	|Product ID/Adcode		|10				|A				|YES		|								|
|19	|Inbound # Dialed		|10				|A				|No		|								|
|20	|Transaction Time		|6				|N				|No		|HHMMSS								|
|21	|Transaction Date		|8				|N				|Yes		|MMDDYYYY							|
|22	|Operator Code			|3				|A				|No		|								|
|23	|Ship To First Name		|11				|A				|Yes		|The first name and last name fields are a total of 22 characters combined---so the length of each can be adjusted as needed and as long as the total does not go past 22 they will not be truncated. |
|24	|Ship To Last Name		|11				|A				|Yes		|								|
|25	|Ship To Address #1		|30				|A				|Yes		|								|
|26	|Ship To Address #2		|30				|A				|No		|								|
|27	|Ship To Address #3		|30				|A				|No		|								|
|28	|Ship To City			|13				|A				|Yes		|								|
|29	|Ship To State			|2				|A				|Yes		|								|
|30	|Ship To Zip Code		|11				|A				|Yes		|								|
|31	|Ship To Country		|35				|A				|No		|								|
|32	|Number of Payments		|1				|N				|Yes		|POPULATE ALL WITH "1"						|
|33	|Delivery Method		|1				|A				|No		|DO NOT USE UNLESS SPECIFIED BY FOSDICK				|
|34	|Order Base Amount		|9				|N				|YES		|POPULATE ALL WITH "0.00"					|
|35	|Shipping & Handling Charge	|8				|N				|YES		|POPULATE ALL WITH "0.00"					|
|36	|Tax				|8				|N				|YES		|POPULATE ALL WITH "0.00"					|
|37	|Discount			|8				|N				|YES		|POPULATE ALL WITH "-0.00"					|
|38	|Order Total			|9				|N				|YES		|POPULATE ALL WITH "0.00"					|
|39	|Email Address			|40				|A				|No		|								|
|40	|Micr #				|35				|A				|No		|								|
|41	|Check #			|8				|A				|No		|								|
|42	|Bank Name			|30				|A				|No		|								|
|43	|Bank City			|30				|A				|No		|								|
|44	|Ship-To Phone #		|10				|A				|No		|								|
|45	|Bank Account Type		|1				|A				|No		|								|
|46	|Filler				|1				|A				|No		|								|
|47	|Filler				|1				|A				|No		|								|
|48	|Filler				|1				|A				|No		|								|
|49	|Filler				|1				|A				|No		|								|
|50	|Filler				|1				|A				|No		|								|

## Trailer Record
Each file must also have a trailer record that provides information about the file to fosdick, this record will meet the following format standards:

|Field	|Description		|Size (max. # of char.)	|Type (N=Number, A=Text)	|Required	|Picture/Notes						|
|-------|-----------------------|-----------------------|-------------------------------|---------------|-------------------------------------------------------|
|1	|Trailer Record		|Constant		|A				|Yes		|TRAILER RECORD						|
|2	|File Name		|36			|A/N				|Yes		|							|
|3	|Date			|8			|N				|Yes		|YYYYMMDD						|
|4	|Time			|6			|N				|Yes		|HHMMSS							|
|5	|Number of Records	|25			|N				|Yes		|Include trailer record in this count			|
|6	|Sequence Number	|5			|N				|Yes		|Example:  First file = 00001, second file = 00002 etc…	|
