# ACE RoleManager Bot

Discord bot automático para asignar roles basado en compras de WooCommerce y SureCart.

## Configuración Rápida

### 1. Obtén tu BOT_TOKEN
- Ve a Discord Developer Portal
- - Application ID: 1455365984318914722
  - - Copia el BOT_TOKEN
   
    - ### 2. Obtén tu GUILD_ID
    - - Abre Discord
      - - Click derecho en "Comunidad ACE"
        - - Copia el ID del servidor
         
          - ### 3. Crea tu WEBHOOK_SECRET
          - - Cualquier contraseña que quieras (ej: "ace_secret_12345")
           
            - ### 4. Deploy en Render.com (Fácil y Gratis)
           
            - 1. Ve a https://render.com
              2. 2. Nueva Web Service
                 3. 3. Conecta tu repositorio GitHub
                    4. 4. Lenguaje: Python
                       5. 5. Build: `pip install -r requirements.txt`
                          6. 6. Start: `python main.py`
                             7. 7. Variables de entorno:
                                8.    - BOT_TOKEN = (tu token)
                                      -    - GUILD_ID = (ID del servidor)
                                           -    - WEBHOOK_SECRET = (tu contraseña)
                                            
                                                - 8. Deploy
                                                 
                                                  9. ### 5. Prueba
                                                  10. - Haz una compra de prueba
                                                      - - Revisa los logs en Render
                                                        - - El role debería aparecer automáticamente en Discord
                                                         
                                                          - ## Productos Mapeados
                                                         
                                                          - **WooCommerce (15 Cursos)**
                                                          - - IDs: 8087, 7648, 7640, 7635, 7630, 7625, 7620, 7615, 7610, 7602, 7599, 7595, 7588, 7583, 6424
                                                            - - Role: Single-Course
                                                              - - Precio: $40 USD
                                                               
                                                                - **SureCart (Club)**
                                                                - - ID: d471f5fb-0f48-4f9d-97f4-95638ef57dac
                                                                  - - Role: Miembro-Club-ACE
                                                                    - - Precio: $25 USD/mes
                                                                     
                                                                      - ## URL del Webhook
                                                                      - `https://[tu-url-render]/webhook`
                                                                     
                                                                      - Agregar header: `X-Webhook-Secret: [tu-secreto]`
