import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
from auth import authenticator

#Création de la barre sur le coté
with st.sidebar:
  # Création du menu qui va afficher les choix
  selection = option_menu(
              menu_title=None,
              options = ["Accueil", "Photos"]
        )
# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.title("Bienvenue sur la page d'accueil !")
    st.header("L'ami des chats")
    st.image("https://www.leparisien.fr/resizer/KAdHG3AhLuFJYkI9bqPRmhk4-gU=/932x582/arc-anglerfish-eu-central-1-prod-leparisien.s3.amazonaws.com/public/CA6L5R6SNOC3STVEIM2NI4BJWM.jpg")
      
    # On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
    # L'utilisateur peut choisir son moyen de contact préféré parmi trois options
    add_selectbox = st.sidebar.selectbox(
        "Comment tu vas ?", # Question affichée
        ("Super bien", "Bien", "C'est pas ma journée") # Options proposées
    )

    # Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
    with st.sidebar:
        # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
        add_radio = st.radio(
            "Pourquoi est tu ici",  # Titre de la question
            ("Pour faire Coucou", "Rien de mieu à faire")  # Choix proposés
        )
      
      
      
elif selection == "Photos":
  authenticator.login(location="main")
  def accueil():
        
      st.title("Bienvenue dans l'album privé de mon chat, là ou il post tous ses sefies", text_alignment="center")
      # Création de 3 colonnes 
      col1, col2, col3 = st.columns(3, border=True)
      
      with col1:
        st.header("My band", text_alignment="center")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOYrncpznPI9EIM_g62HlWM4OM6VoXHRwd1g&s", use_container_width=True)

      with col2:
        st.header("Au zoo avec mon oncle", text_alignment="center")
        st.image("https://www.watson.ch/fr/imgdb/37e1/Qx,A,0,0,984,672,410,280,164,112/2374061013599647", use_container_width=True)

      with col3:
        st.header("Grimace", text_alignment="center")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6Le0znSW4L5PSsc5_NZ6ciWymyocZdCP8cA&s", use_container_width=True)


  if st.session_state["authentication_status"]:
    accueil()
    
    with st.sidebar:
      # Le bouton de déconnexion
      authenticator.logout(location="main")

  elif st.session_state["authentication_status"] is False:
      st.error("L'username ou le password est/sont incorrect")
  elif st.session_state["authentication_status"] is None:
      st.warning('Les champs username et mot de passe doivent être remplie')
      
      




  
