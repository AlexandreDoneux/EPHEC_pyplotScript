class LineSyntaxError(Exception):
    """
    Erreur pour indiquer un problème de format sur une certaine ligne.
    """
    def __int__(self, line="None"):
        self.line = line


def clean_lines(all_lines):
    """
    Fonction supprimant les valeurs doublons dans une liste de lignes d'un fichier.
    :param - all_lines: Liste contenant les lignes du fichier texte analysé.
    :return - clean_lines: Liste des lignes sans doublons
    """
    new_lines = []  # liste des lignes sans les doublons
    first_line = True
    for line in all_lines:
        line = line.strip("\n")
        line = line.strip()  # .strip() -> on enlève les espaces en trop au début et à la fine

        if first_line:
            previous_line = line
            first_line = False
            new_lines.append(line)
            continue  # on ne peut pas verifier un doublon à la première ligne

        # On saute l'écriture dans la nouvelle liste les lignes en doublon l'une à la suite des autres.
        # Notamment les doubles lignes vides
        if line == previous_line:
            continue

        new_lines.append(line)
        previous_line = line

    return new_lines

def draw(main_list):
    """

    """
    color_list = ["goldenrod", "blueviolet", "crimson", "navy", "seagreen", "steelblue", "maroon", "coral",
                  "olivedrab", "lime", "darkorange", "aqua", "dimgray", "cornflowerblue"]

    for group in main_list:
        draw_color = color_list[randint(0, len(color_list) - 1)]
        if len(group) == 1:
            group[0].draw_point(markerfacecolor=draw_color)  # Quand un seul point on le dessine avec Point.draw_point()
            continue
        my_figure = Figure(group)
        my_figure.draw_figure(color=draw_color)

def group_figures(all_lines):
    """
    Fonction qui prends en paramètres une liste des lignes du fichier à analyser. Renvoie une liste de listes. La
    fonction supprime les lignes doublons les unes à la suite des autres. Les différentes listes représentent les
    groupements de figures. Les groupements sont déterminés par les lignes vides dans le fichier texte analysé.
    :param - all_lines: Liste des lignes du fichier.
    :return - grouped_points: Liste contenant une liste pour chaque groupement de points.
    """
    main_list = []  # liste qui contiendra les groupes
    i = 0
    # indice de main_list. On aura main_list = [[point1, point2],[point3],[........],[.........]]
    # l'indice augmentera de 1 lorsqu'on tombe sur une liste vide -> début d'une nouvelle figure

    maxx = 0
    minx = 0
    maxy = 0
    miny = 0

    new_lines = clean_lines(all_lines)

    # on retire la première ligne si c'est une ligne vide
    if new_lines[0] == "":
        new_lines = new_lines[1:]

    # on pré-construit l'array final avec les groupements de points
    number_of_groups = new_lines.count("")
    for j in range(number_of_groups):
        main_list.append([])

    for line in new_lines:
        if line == "":
            i += 1  # on commence une nouvelle sous-liste
            continue

        line = line.split()  # division en une liste

        # Vérification de si la liste a la bonne taille.
        if len(line) != 3:
            print("Erreur taille")
            raise LineSyntaxError(line)


        # marche pas pour l'instant
        # Vérification de si les valeurs dans une ligne sont justes
        try:
            float(line[1])
            float(line[2])
        except ValueError:
            print("Erreur type")
            raise LineSyntaxError(line)


        line[1] = float(line[1])
        line[2] = float(line[2])

        if line[1] > maxx:
            maxx = line[1]
        if line[2] > maxy:
            maxy = line[2]
        if line[1] < minx:
            minx = line[1]
        if line[2] < miny:
            miny = line[2]

        # Création du point dans la sous-liste
        main_list[i].append(Point(line[0], line[1], line[2]))

    extremes = [minx, maxx, miny, maxy]

    return main_list, extremes