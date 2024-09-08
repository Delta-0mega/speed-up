from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.video.fx.all as vfx
import os
import fade
from colorama import Fore
os.system('cls' if os.name == 'nt' else 'clear')
sp = "output\speedup"
def create_output_dirs():
    os.makedirs(os.path.join(sp, "mp3"), exist_ok=True)
    os.makedirs(os.path.join(sp, "mp4"), exist_ok=True)
def process_video(input_path, output_name, keep_audio_only):
    clip = VideoFileClip(input_path)
    if keep_audio_only:
        audio_output_path = os.path.join(sp, "mp3", f"{output_name}.mp3")
        speedup_audio = clip.audio.fx(vfx.speedx, factor=1.1)
        speedup_audio.write_audiofile(audio_output_path)
        print(f"Audio extrait et accéléré sauvegardé sous : {audio_output_path}")
        return audio_output_path
    else:
        speedup_clip = clip.fx(vfx.speedx, factor=1.1)
        video_output_path = os.path.join(sp, "mp4", f"{output_name}.mp4")
        speedup_clip.write_videofile(video_output_path, codec="libx264")
        print(f"Vidéo accélérée sauvegardée sous : '{video_output_path}'")
        return video_output_path
def process_audio(input_path, output_name):
    audio_clip = AudioFileClip(input_path)
    speedup_audio = audio_clip.fx(vfx.speedx, factor=1.1)
    audio_output_path = os.path.join(sp, "mp3", f"{output_name}.mp3")
    while True:
        speedup_audio.write_audiofile(audio_output_path)
        print(f"Audio accéléré sauvegardé sous : '{audio_output_path}'")
        return audio_output_path
def main():
    create_output_dirs()
    banner = """

   ▄████████    ▄███████▄    ▄████████    ▄████████ ████████▄       ███    █▄     ▄███████▄ 
  ███    ███   ███    ███   ███    ███   ███    ███ ███   ▀███      ███    ███   ███    ███ 
  ███    █▀    ███    ███   ███    █▀    ███    █▀  ███    ███      ███    ███   ███    ███ 
  ███          ███    ███  ▄███▄▄▄      ▄███▄▄▄     ███    ███      ███    ███   ███    ███ 
▀███████████ ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀     ███    ███      ███    ███ ▀█████████▀  
         ███   ███          ███    █▄    ███    █▄  ███    ███      ███    ███   ███        
   ▄█    ███   ███          ███    ███   ███    ███ ███   ▄███      ███    ███   ███        
 ▄████████▀   ▄████▀        ██████████   ██████████ ████████▀       ████████▀   ▄████▀      
                                                                                            
    
"""
    print(fade.fire(banner))
    input_path = input(Fore.YELLOW + "Entrez le chemin du fichier (vidéo ou audio) : ").strip('"')  # Enlève les guillemets si présents
    output_name = input(Fore.YELLOW + "Entrez le nom de sortie (sans extension) : ")
    file_extension = os.path.splitext(input_path)[1].lower()
    if file_extension in ['.mp4', '.mov', '.avi', '.mkv']:
        keep_audio_only = input(Fore.YELLOW + "Souhaitez-vous conserver uniquement l'audio ? (y/n) : ").lower() == 'y'
        result = process_video(input_path, output_name, keep_audio_only)
    elif file_extension == '.mp3':
        result = process_audio(input_path, output_name)
    else:
        print(Fore.RED + "Format non pris en charge. Veuillez entrer un fichier vidéo ou MP3.")
        return
    print(Fore.GREEN + f"Traitement terminé. Fichier généré : {result}")
if __name__ == "__main__":
    main()
