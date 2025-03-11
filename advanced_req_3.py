import streamlit as st
import pandas as pd
import subprocess

#process = subprocess.Popen([
#    "streamlit", "run", "adv_req_3.py",
#    "--server.port", "707",
#    "--server.headless", "true"
#])

# Load Data
file_path = 'clean.csv'
data = pd.read_csv(file_path)

st.title("23/24 Recommendation System")
st.write("Select a club for a Recommendation")


# Dropdown Selection
teams = sorted(data['Team'].unique())
selected_team = st.selectbox("Select Club:", teams)

# Show selected team
#st.write(f"Selected team: {selected_team}")

# Display recommendation if Arsenal is selected
if selected_team == "Arsenal":
    st.write("Arsenal's starting left winger, Gabriel Martinelli, scored 2 less goals than he should have. "
             "Therefore, it is recommended that they buy a left winger who will closer match his expected goals. "
             "They should buy a world class winger such as Rafael Leão from AC Milan. "
             "This would close the gap to Manchester City.")
    st.image("https://total-italianfootball.com/wp-content/uploads/2023/06/Screenshot-2023-06-05-at-16.13.22.png", caption="Rafael Leão")
   
elif selected_team == "Aston Villa":
    st.write("Aston Villa's star striker, Ollie Watkins, was responsible for 1/4 of their goals. "
             "Therefore, it is recommended that they give their young back up striker Jhon Duran more minutes. "
             "In limited minutes he scored 5 goals. This is likely to prevent Watkins from getting injured"
             "This would allow them to maintain their champions league level.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/jhon-duran-aston-villa-1696871261-118814.jpg", caption="Jhon Duran")
   
elif selected_team == "Bournemouth":
    st.write("Bournemouth's main striker, Dominic Solanke, was responsible for 1/3 of the teams goals with 19. "
             "Therefore, it is recommended that they bring in a backup striker to help Solanke by scoring more goals. "
             "They should buy an experienced player within their budget such as, Boulaye Dia from Salernitana. "
             "This would allow them to push up to the top half of the table.")
    st.image("https://i.eurosport.com/2023/08/28/3772894-76747808-2560-1440.jpg", caption="Boulaye Dia")
   
elif selected_team == "Brentford":
    st.write("Brentford's starting striker, Neal Maupay, scored 3 less goals than he should have. "
             "Therefore, it is recommended that they replace him with a better striker. "
             "They should buy an young and exciting striker to add to their aging team, such as Gift Orban. "
             "This would allow them to push away from the relegation zone.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/gift-orban-olympique-lyon-2023-2024-1040074709hjpg-1709723693-131098.jpg", caption="Gift Orban")
   
elif selected_team == "Brighton and Hove Albion":
    st.write("Brighton were the 4th worse under perfromers as they scored 8.7 less goals than they should have. "
             "Therefore, it is recommended that they add more goals in the midfield area. "
             "They should buy an experienced goal scoring midfielder, such as Lovro Majer. "
             "This would allow them to push up to the top half of the table.")
    st.image("https://www.planetsport.com/image-library/land/700/1675464_lovro-majer-wolfsburg-24-august-202416.webp", caption="Lovro Majer")
   
elif selected_team == "Burnley":
    st.write("Burnley scored the 3rd least amount of goals, and had the 2nd lowest xg, which meant they got relegated. "
             "Therefore, it is recommended that they buy a proven goal scorer to boost these numbers. "
             "They should buy Che Adams, who is a proven championship level goal scorer. "
             "This would help them get promoted back to the premier league from the championship as soon as possible.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/che-adams-torino-2024-2425-1725098032-146850.jpg", caption="Che Adams")
   
elif selected_team == "Chelsea":
    st.write("Chelsea were heavily relient on cole palmer last season as he scored 1/3 of their goals. "
             "Therefore, it is recommended that they buy world class striker to add more goals to the team apart from Cole Palmer. "
             "They should buy Victor Osimhen, who is a proven champions league level goal scorer. "
             "This would help them get push for top 4 and a champions leage spot.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/victor-osimhen-ssc-neapel-2022-1665600735-94105.jpg", caption="Victor Osimhen")
   
elif selected_team == "Crystal Palace":
    st.write("Crystal Palace over scored their xg by 6+ goals. "
             "Therefore, it is recommended that they buy a more creative midfielder as they are heavily relient on their front 3. "
             "They should get Arda Güler on loan, who is an exciting wonderkid from Real Madrid to help support their attack. "
             "This would help them get push for the top half.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/arda-guler-real-madrid-2023-2024-1711029152-132371.jpg", caption="Arda Güler")


elif selected_team == "Everton":
    st.write("Everton were the worst under performers in the league as they scored 15 less goals than they should have. "
             "Therefore, it is recommended that they buy a clinical striker to score the chances they create. "
             "They should get Armando Broja, who is a cheap, powerful and clinical striker. "
             "This would help them get push away from the relegation zone.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/armando-broja-chelsea-2022-1668701789-96819.jpg", caption="Armando Broja")
   
elif selected_team == "Fulham":
    st.write("Fulham only had an xg of 51 goals, which is not a lot. "
             "Therefore, it is recommended that they buy a creative midfielder to create more chances. "
             "They should get Emile Smith Rowe, who is a young and cheap attacking midfielder to support their attack. "
             "This would help them get push towards the top half.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/emile-smith-rowe-fc-arsenal-1633362574-72126.jpg", caption="Emile Smith Rowe")
   
elif selected_team == "Liverpool":
    st.write("Liverpool had the highest expected goals in the league with 90, but only scored 80. "
             "Therefore, it is recommended that they renew their top scorer's, Mohamed Salah, contract as it expires next year. "
             "They should also replace Darwin Nuñez with a better striker as he underscored his xg by over 5. "
             "They should buy world class striker Lautaro Martinez who will help finish the chances that Nuñez missed. "
             "This would help them fight for the title next year.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/mohamed-salah-liverpool-2021-1632687357-71713.jpg", caption="Mohamed Salah")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/lautaro-martinez-inter-2022-1660303713-90070.jpg",caption="Lautaro Martinez")
   
elif selected_team == "Luton Town":
    st.write("Luton Town over scored their xg by 5 goals. "
             "Therefore, it is recommended that they buy a creative midfielder to maintain this level of scoring. "
             "They should get Flynn Downes, who is a young and cheap attacking midfielder help their starting strikers. "
             "This would help them get promoted from the championship as soon a possible.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/flynn-downes-west-ham-united-2022-1657220307-88114.jpg", caption="Flynn Downes")

elif selected_team == "Manchester City":
    st.write("Manchester City were the biggest over achievers in terms of goals scorer at 11 over their xg. "
             "Therefore, it is recommended that they buy a new right winger as they lack depth in that spot. "
             "They should buy Khvicha Kvaratskhelia, an explosive, techincal dribbler who can score with both feet. "
             "This will help maintain their champions status.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/khvicha-kvaratskhelia-georgien-2024-1719433954-140983.jpg",caption="Khvicha Kvaratskhelia")
   
elif selected_team == "Manchester United":
    st.write("Manchester United have an over relience on Bruno Fernandes with 10 goals. "
             "Therefore, it is recommended that they buy a backup attacking midfielder to try help Fernandes. "
             "They should buy Paulo Dybala, an experienced attacking midfielder who can play striker if needed. "
             "This will help them push for a European spot.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/paulo-dybala-roma-2023-24-1707214945-128622.jpg",caption="Paulo Dybala")
   
elif selected_team == "Newcastle United":
    st.write("Newcastle United were the 3rd best attacking team in goals scored and 4th most xg. "
             "Therefore, it is recommended that they buy a bquick winger to bolster the attacking depth. "
             "They should buy Noni Madueke, a rapid winger who can deliver great crosses to the main striker Isak. "
             "This will help them push for better European spots.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/madueke-noni-2023-2024-chelsea-1034032312hjpg-1697041323-118972.jpg",caption="Noni Madueke")
   
elif selected_team == "Nottingham Forest":
    st.write("Nottingham Forest only scored 49 goals this season. "
             "Therefore, it is recommended that they buy a more dynamic winger to have a complete front 3. "
             "They should buy Amad Diallo, an explosive winger who can score and create chances. "
             "This will help them push out of the relegation zone.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/amad-diallo-manchester-united-1617106698-59739.jpg",caption="Amad Diallo")
   
elif selected_team == "Sheffield United":
    st.write("Sheffield United had the lowest goals scored with 31 and the lowest xg with 40. "
             "Therefore, it is recommended that they buy a leathal striker to score more goals. "
             "They should buy Ben Brereton Díaz, an physical, proven championship goal scorer. "
             "This will help them get promoted to back to the premier league quickly.")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/ben-brereton-chile-2022-1643372637-79316.jpg",caption="Ben Brereton Díaz")
   
elif selected_team == "Tottenham Hotspur":
    st.write("Tottenham Hotspur only had 2 players that scored over 10 goals last season. "
             "Therefore, they should buy a new winger to provide compitition to Dejan Kulusevski who can be very inconsistent. "
             "They should buy Pedro Gonçalves, a portugese winger who can also play in attacking midfield and averages 14  goal contributions per season. "
             "This would help them push for a top 4 position and a champions league spot. "
             )
    st.image("https://tmssl.akamaized.net/images/foto/galerie/pedro-goncalves-sporting-2023-1676924843-102309.jpg",caption="Pedro Gonçalves")
    
elif selected_team == "West Ham United":
    st.write("West Ham United were heavily relient on their winger Jarrod Bowen who scored 1/3 of the teams goals with 16/58. "
             "Therefore, it is recommended that they bring in a top tier striker to help add more goals to the squad. "
             "They should buy Jonathan David, an experienced striker who averages 15 goals per season. "
             "This would help them push for a European spot. "
             )
    st.image("https://tmssl.akamaized.net/images/foto/galerie/jonathan-david-lille-osc-1637705769-75337.jpg",caption="Jonathan David")
    
elif selected_team == "Wolverhampton Wanderers":
    st.write("Wolverhampton Wanderers only had an ex of 49.5 goals. "
             "Therefore, it is recommended that they buy a creative midfielder to create more chances. "
             "They should buy Álex Baena, a spanish attacking midfielder who can also play on the wing as an depth option. "
             "This would help them push for the top half of the table. ")
    st.image("https://tmssl.akamaized.net/images/foto/galerie/alex-baena-spain-euro-2024-1720794511-142334.jpg", caption="Álex Baena")