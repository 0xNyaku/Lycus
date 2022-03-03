# by billythegoat356

# https://github.com/billythegoat356/Phobos


from pystyle import Anime, Colors, Colorate, System, Center, Write
from pydorks import GoogleSearch


# intext:XXX movie site:drive.google.com
# XXX -inurl:(htm|html|php|pls|txt) intitle:index.of “last modified” (mp4|wma|aac|avi)


def search(movie_name: str) -> str:
    movie = GoogleSearch.search(results_len=1, intext=movie_name + " movie", site='drive.google.com')
    return "".join(movie[0].split('&')[0]) if len(movie) == 1 else False




banner = r"""
                                 :!    :*                              
                                 %$  : :@!:                            
                                @/@*@#&*@§$               %! %!        
                             :*!##/§§§§§§§&!*!          **@$*#*$!      
                             :!!!&§§§§/§§#*!%* :!       :###/##*       
                            :!!!:$§§§§§§§&$%%$%%!:      :§§§§§@$*:     
                         *!:!$$$&*$§§§§§#&/#§&@%!!!:   %&§§§/&*::      
                       ::!%$@#/#/§§§§§§§§§§§§§§§@!! :*@§§§§/%:         
                       :!!%$#/§§§§§§§§§§§§§§§§§§§#&@/§§§§§/$           
                        :::$§§§§§§§§§§§§§§§§§§§§§§§§§§§§/!:            
       *:!::             *!#§§§§§§§§§§§§§§§§§§@@/§§§§§/%:              
       @/&&!             %/§§§§§§§§§§§§§§§§§§&  :*§#&*:                
       :@§§#$*!:        $/§§§§§§§§§§§§§§§§§§/:   :!                    
         !%&§§§/&###&&##§§§§§§@@§§§§§§§§§§§§@                          
            *@/§§§§§§§§§§§§/#&&&§§§§§§§§§§§§§@!:                       
              :$&##/§§§§§§%%§§§§§§§§§§§§§§§§§§§@:                      
                   :**!!*$@&§§§§§§§§§§§§§§§§§§§/$*                     
                        :&$§§§§§§§§§§§§§§§§§§§§§@&%                    
                        !$#§§§§§§§§§§§§§§§§§§§§§@:%                    
                       :&§§§§§§§§§§§§§§§§§§§§§§§/::                    
                       $§§§§§§§§§§§§§§§§§§//§§§§/!                     
                     :$/§§§§§§§§§§§§§§§§§§§§§§§§#::                    
                !**%@§§§§§§§§§§§§§§§/§§§§§§§§§§§#:: :                  
               :*/§§§§§§§§§§§§§§§§§§/§§§§§§§§§§§&                      
               !$/@#§§§§§§§§§§§§§§§§§§§§/&§§§§§§&                      
             :$@&&#/§§§§§§§§§§§§§§§§§/§§§@§§§§§§@**:                   
            **%$§§/§§§§§§§§§§§§§§§§§#!/§§§§§§§§§$&:                    
              %#§§§§§§§§§§§§§§§§§§/§# $§#/§§§§§@$/:                    
          :!$###§§§§§§##§§§§§§§§§§&%/%#@$/§§§§§$@§!                    
       :%&§§§§/§§§§§#% :@§§/&§§§§§%*§!&#/§§§§§§§/%                     
     !@#/#&&@*&$#§§%    *§§@ /§§§§%!$:%$§§§§§§§§*                      
   !*%*!:  :    */*     :#§! !&§§§&    $§§§§§§§#!                      
  ::           *@*       :@*  :/§§§@   &/§§§§§§:                       
               :           :  !/§§§&   *§§§§§/$                        
                              *§§§§&   $§§§§§%                         
                              $§§§§$  :&/§§§§%                         
                              @§§§§@   *§§§§&!                         
                              @§§§§& :@/§§§#                           
                              :@/§§$ :/§§§§&                           
                                !%&:  *§§§§$                           
                                  :   :/§§§%                           
                                      :/§§#!                           
                                      :#§§@                            
                                       :#§$                            
                                        :*$                            
                                          :                            """[1:]


ascii_art = r"""
                    :888888888                                                           
                  :88888::::888                                                          
                 88888     :888                                                          
                88888    888888                                                          
               88888     8888:                                                           
              :8888       :                                                              
              8888:                                                                ::    
             88888                                                              :8888:   
             8888:             8888     8888      :888888:    :8888    8888:    88888    
            88888            888888:   88888   :8888888888   888888  :88888:   888888    
           :8888           :8888888  88888  :88888: 88888 8888888:   88888  :8888888:   
           8888           88888888  88888  888888  :88:  88888888   88888  8888 :888:  :
   :888:  8888:          888:8888  888888 :88888:       888888888   88888 :888   8888 888
 888888888888:         88:::8888  888888 888888:      8888 88888   88888 888:    8888888:
888:  :888888:       :888  8888  88888888888888     8888: :8888:  888888888:88 :888888:  
888 ::888888888888888888  888888888888888 :8888::88888:   888888888888888:8888888888:    
888888888: :88888888888   :88888:888888    :88888888:     :88888  88888: :8888888:       
  :88:         :88::         :  88888         :::           :       :      :             
                               88888                                                     
                              88888                                                      
                             88888                                                       
                            88888                                                        
                           :8888:                                                        """[1:]



def init():
    System.Clear()
    System.Size(160, 50)
    System.Title("Phobos")
    Anime.Fade(text=Center.Center(banner), color=Colors.red_to_green, mode=Colorate.Vertical, enter=True)




def main():
    System.Clear()
    print('\n'*2)
    print(Colorate.Diagonal(color=Colors.red_to_green, text=Center.XCenter(ascii_art)))
    print('\n'*3)
    movie_name = Write.Input(text="Enter the name of the movie you want to download -> ", color=Colors.red_to_green, interval=0.005)
    print()
    movie_link = search(movie_name=movie_name)

    if movie_link:
        Write.Print(text="Here you go: ", color=Colors.red_to_green, interval=0.005)
        Write.Input(text=movie_link, color=Colors.white, interval=0.005)
        return exit()
    else:
        Write.Input(text=f"Sorry mate, I didn't find anything!", color=Colors.red_to_green, interval=0.005)
        return


if __name__ == '__main__':
    init()
    while True:
        main()
