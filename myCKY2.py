import gram

# Le bien qu’il fait, il le fait bien.
w1 = [ "le ", "bien ", "qu ", "il ", "fait ", "_virgule_ ", "il ", "le ", "fait ", "bien ", "_point_ "]
# Le fait est que j’ai peu de biens.
w2 = [ "le ", "fait ", "est ", "que ", "j ", "ai ", "peu ", "de ", "biens ", "_point_ "]
# J’ai bien du mal à faire ce que les autres font bien.
w3 = [ "j ", "ai ", "bien ", "du ", "mal ", "a_ ", "faire ", "ce ", "que ", "les ", "autres ", "font ", "bien ", "_point_ "]
# Bien des gens ont fait un peu de bien.
w4 = [ "bien ", "des ", "gens ", "ont ", "fait ", "un ", "peu ", "de ", "bien ", "_point_ "]
# Bien qu’il ait fait du bien, il ne l’ a pas bien fait.
w5 = [ "bien ", "qu ", "il ", "ait ", "fait ", "du ", "bien ", "_virgule_ ", "il ", "ne ", "l ", "a ", "pas ", "bien ", "fait ", "_point_ "]

phrase = w5

estDansLG1, gram.E1 = gram.testeMot(gram.g0, phrase)
gram.prettyPrintUnderMatShape(gram.E1, phrase)
