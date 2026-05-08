import pygame
import random

# --- 1. SETUP INIZIALE ---
pygame.init()
pygame.mixer.init() # Motore audio

# Colori di sicurezza
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)

# Dimensioni dello schermo
SCHERMO_WIDTH = 800
SCHERMO_HEIGHT = 600
BLOCCO_SIZE = 20 # Grandezza di ogni "pallina"

schermo = pygame.display.set_mode((SCHERMO_WIDTH, SCHERMO_HEIGHT))
pygame.display.set_caption('SNAKE iperfigo - By GP')

# Font per i testi
font_punti = pygame.font.SysFont('Arial', 30, bold=True)
font_game_over = pygame.font.SysFont('Arial', 60, bold=True)

orologio = pygame.time.Clock()

# --- 2. GESTIONE IMMAGINI E SUONI ---
def carica_immagine(nome_file, larghezza, altezza):
    try:
        immagine = pygame.image.load(nome_file)
        immagine = pygame.transform.scale(immagine, (larghezza, altezza))
        return immagine
    except:
        # Se non metti le foto nella cartella, crea dei quadratini colorati in automatico!
        immagine = pygame.Surface((larghezza, altezza))
        immagine.fill(random.choice([(255,0,0), (0,255,0), (0,0,255)]))
        return immagine

testa_img = carica_immagine('testa.png', BLOCCO_SIZE, BLOCCO_SIZE)
corpo_img = carica_immagine('corpo.png', BLOCCO_SIZE, BLOCCO_SIZE)
mela_img = carica_immagine('mela.png', BLOCCO_SIZE, BLOCCO_SIZE)

# Audio
try:
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play(-1)
    suono_crunch = pygame.mixer.Sound('crunch.wav')
    suono_boom = pygame.mixer.Sound('boom.wav')
except:
    suono_crunch = None
    suono_boom = None

# --- 3. IL MOTORE DEL GIOCO ---
def loop_gioco():
    gioco_in_corso = True
    punti = 0
    VELOCITA = 8 # <-- VELOCITÀ RALLENTATA E GIUSTA!
    
    # Coordinate di partenza (Uso // per forzare numeri interi senza virgola)
    x = SCHERMO_WIDTH // 2
    y = SCHERMO_HEIGHT // 2
    x_change = BLOCCO_SIZE
    y_change = 0
    
    serpente_coords = [[x, y]]
    
    # Mela generata esattamente sulla griglia matematica
    cibo_x = random.randint(0, (SCHERMO_WIDTH - BLOCCO_SIZE) // BLOCCO_SIZE) * BLOCCO_SIZE
    cibo_y = random.randint(0, (SCHERMO_HEIGHT - BLOCCO_SIZE) // BLOCCO_SIZE) * BLOCCO_SIZE
    
    while gioco_in_corso:
        # --- A. Tasti premuti ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return -1 # Chiude la finestra del tutto
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_change != BLOCCO_SIZE:
                    x_change = -BLOCCO_SIZE
                    y_change = 0
                elif evento.key == pygame.K_RIGHT and x_change != -BLOCCO_SIZE:
                    x_change = BLOCCO_SIZE
                    y_change = 0
                elif evento.key == pygame.K_UP and y_change != BLOCCO_SIZE:
                    y_change = -BLOCCO_SIZE
                    x_change = 0
                elif evento.key == pygame.K_DOWN and y_change != -BLOCCO_SIZE:
                    y_change = BLOCCO_SIZE
                    x_change = 0
        
        # --- B. Movimento ---
        x += x_change
        y += y_change
        nuova_testa = [x, y]
        
        # --- C. Controllo Morte (Bordi o auto-morso) ---
        if x >= SCHERMO_WIDTH or x < 0 or y >= SCHERMO_HEIGHT or y < 0:
            if suono_boom: suono_boom.play()
            return punti

        if nuova_testa in serpente_coords:
            if suono_boom: suono_boom.play()
            return punti

        # --- D. Aggiornamento Corpo e Mela ---
        serpente_coords.insert(0, nuova_testa)
        
        if x == cibo_x and y == cibo_y:
            punti += 100
            if suono_crunch: suono_crunch.play()
            cibo_x = random.randint(0, (SCHERMO_WIDTH - BLOCCO_SIZE) // BLOCCO_SIZE) * BLOCCO_SIZE
            cibo_y = random.randint(0, (SCHERMO_HEIGHT - BLOCCO_SIZE) // BLOCCO_SIZE) * BLOCCO_SIZE
        else:
            serpente_coords.pop() # Se non mangia, taglia la coda
            
        # --- E. Grafica ---
        schermo.fill(NERO) # Colora lo sfondo di nero
        
        schermo.blit(mela_img, (cibo_x, cibo_y)) # Disegna mela
        
        for pezzo in serpente_coords[1:]:
            schermo.blit(corpo_img, (pezzo[0], pezzo[1])) # Disegna corpo
            
        schermo.blit(testa_img, (serpente_coords[0][0], serpente_coords[0][1])) # Disegna testa
        
        # Testo Punti
        testo_punti = font_punti.render(f'Punti: {punti}', True, BIANCO)
        schermo.blit(testo_punti, (10, 10))
        
        pygame.display.flip() # Aggiorna lo schermo
        orologio.tick(VELOCITA) # Regola la velocità del serpente

# --- 4. CICLO PRINCIPALE E GAME OVER ---
while True:
    punti_finali = loop_gioco()
    
    if punti_finali == -1: # Se l'utente ha premuto la X rossa della finestra
        break
        
    # Schermata di Game Over pulita
    schermo.fill(NERO)
    testo1 = font_game_over.render('GAME OVER!', True, ROSSO)
    testo2 = font_punti.render(f'Punti: {punti_finali} - Premi SPAZIO per riprovare', True, BIANCO)
    
    rect1 = testo1.get_rect(center=(SCHERMO_WIDTH//2, SCHERMO_HEIGHT//2 - 30))
    rect2 = testo2.get_rect(center=(SCHERMO_WIDTH//2, SCHERMO_HEIGHT//2 + 30))
    
    schermo.blit(testo1, rect1)
    schermo.blit(testo2, rect2)
    pygame.display.flip()
    
    # Aspetta che premi SPAZIO per ricominciare
    aspettando = True
    while aspettando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    aspettando = False # Esce dal loop di attesa e riparte il gioco!

pygame.quit()