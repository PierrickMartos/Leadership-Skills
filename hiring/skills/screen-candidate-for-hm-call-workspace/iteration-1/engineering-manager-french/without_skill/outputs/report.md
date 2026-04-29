# Screening Report - Candidat Engineering Manager, equipe Platform

**Poste** : Engineering Manager - Equipe Platform (8 devs, 2 tech leads)
**Entreprise** : Editeur SaaS francais, scale-up ~150 personnes
**Date** : 2026-04-01

---

## 1. Synthese rapide

| Critere | Evaluation | Commentaire |
|---------|-----------|-------------|
| Experience management | Partiel | 2 ans de tech lead avec 5 personnes, mais pas d'EM formel |
| Background technique | Fort | Datadog + Criteo = environnements techniques exigeants |
| Environnement produit | Fort | Datadog et Criteo sont des boites produit matures |
| Anglais courant | Probable | Datadog Paris = contexte international, a verifier |
| Perf management | A creuser | Aucune evidence directe |
| Gestion de roadmap produit | A creuser | Participation probable mais scope a clarifier |

**Verdict preliminaire** : Profil prometteur mais avec des zones d'ombre significatives. Le parcours Criteo -> Datadog est solide. Le risque principal est le passage reel de "tech lead qui manage" a "manager a plein temps". Un call structure est indispensable pour trancher.

---

## 2. Points forts du profil

### Environnements de reference
Criteo et Datadog sont deux des meilleures boites tech en France. Les standards d'engineering y sont eleves, les process matures. Un candidat qui a survecu et progresse dans ces environnements a ete expose a de bonnes pratiques : code review rigoureuse, CI/CD, oncall, incident management, planning trimestriel.

### Progression de carriere coherente
Dev agence (3 ans) -> Senior dev Criteo (4 ans avec promotion) -> Tech Lead Datadog (2 ans). C'est une trajectoire ascendante reguliere, pas de saut inexplique. La promotion interne chez Criteo montre une reconnaissance par les pairs et le management.

### Exposition au management
Chez Datadog : rituels agile, 1:1, recrutement. Ce n'est pas du management a plein temps, mais c'est plus que beaucoup de tech leads. Il a deja touche aux trois piliers : process, people, hiring.

### Taille d'equipe comparable
Il manage 5 personnes actuellement. Passer a 8 devs + 2 tech leads est un saut, mais pas un gouffre. Les tech leads existants peuvent absorber une partie de la charge technique.

---

## 3. Zones de risque

### Risque #1 : La transition tech lead -> manager (CRITIQUE)

C'est LE sujet. Beaucoup de tech leads pensent vouloir devenir manager, puis regrettent de ne plus coder. Questions a poser :

- Qu'est-ce qui le motive dans le passage a l'EM ? (Chercher des reponses sur le people development, pas sur "je veux plus de scope")
- Quelle est la derniere fois ou il a passe une semaine entiere sans ecrire une ligne de code ? Comment l'a-t-il vecu ?
- S'il devait choisir entre debuguer un incident critique en production ou preparer un plan de developpement pour un dev junior, lequel choisirait-il instinctivement ?

**Signal d'alerte** : s'il parle de "garder un pied dans le code", "rester technique", "ne pas devenir un manager bureaucrate". Ce sont des indices qu'il n'est pas pret a lacher.

### Risque #2 : Pas d'experience reelle de perf management (CRITIQUE)

C'est un must-have pour vous. Un tech lead chez Datadog participe probablement aux reviews, mais gerer un PIP (Performance Improvement Plan) ou une conversation de recadrage seul, c'est different. Questions a poser :

- A-t-il deja du annoncer a quelqu'un que sa performance n'etait pas au niveau ? Comment s'y est-il pris ?
- A-t-il deja du gerer un conflit entre deux membres de son equipe ? Quelle a ete sa demarche ?
- A-t-il deja participe ou conduit un processus de sortie (depart negocie, licenciement) ?
- Scenario : "Un dev senior de votre equipe livre regulierement en retard et la qualite baisse depuis 3 mois. Ses collegues commencent a se plaindre. Que faites-vous ?" (Ecouter la structure de sa reponse : est-ce qu'il commence par comprendre ou par sanctionner ?)

### Risque #3 : Saut de scope d'equipe

Passer de 5 a 10 personnes, c'est un changement qualitatif. A 5, on peut tout gerer en direct. A 10, il faut deleguer, structurer, prioriser differemment. Et ici, il aura 2 tech leads a manager -- c'est du management de managers, pas juste du management de devs.

- Comment envisage-t-il sa relation avec les 2 tech leads existants ?
- Comment gere-t-il la delegation aujourd'hui ? A-t-il deja du lacher le controle sur des decisions techniques ?

### Risque #4 : Pas de visibilite externe

Pas de talks, pas de blog. Ce n'est pas eliminatoire, mais ca limite la capacite a evaluer sa pensee structuree et sa communication publique. Cela pourrait aussi indiquer un profil plus introverti -- a mettre en perspective avec le besoin de communiquer avec le product et le leadership.

---

## 4. Guide d'entretien structure (45 min)

### Phase 1 - Mise en contexte (5 min)

Objectif : le mettre a l'aise, comprendre sa motivation.

- "Qu'est-ce qui vous a amene a postuler / repondre a notre approche ?"
- "Qu'est-ce qui vous plait et vous manque dans votre role actuel chez Datadog ?"

**Ecouter** : Est-ce qu'il parle de frustration technique (mauvais signe) ou de desir de plus d'impact sur les personnes (bon signe) ?

### Phase 2 - Management & People (15 min)

Objectif : evaluer la profondeur reelle de son experience people.

**Question 1 - Feedback difficile**
"Racontez-moi une situation ou vous avez du donner un feedback difficile a un membre de votre equipe. Quel etait le contexte, qu'avez-vous dit, et quel a ete le resultat ?"

Bons signaux :
- Il decrit une situation concrete (pas hypothetique)
- Il a prepare la conversation
- Il a ecoute la reaction de la personne
- Il peut decrire le resultat a moyen terme

Mauvais signaux :
- "Ca ne m'est jamais arrive" (= il evite les conversations difficiles)
- Il a delegue a son manager
- Il reste vague

**Question 2 - Performance management**
"Avez-vous deja ete dans une situation ou un membre de votre equipe ne performait pas au niveau attendu sur une periode prolongee ? Comment avez-vous gere ca ?"

Si la reponse est non : "Comment gererez-vous ca quand ca arrivera ? Quelles etapes suivriez-vous ?"

Bons signaux :
- Il mentionne : diagnostic (est-ce un probleme de competence, de motivation, de contexte personnel ?), plan d'action clair, timeline, documentation
- Il parle de fairness envers la personne ET envers l'equipe

Mauvais signaux :
- Il saute directement a "je le mettrais en PIP"
- Il n'evoque jamais la dimension humaine
- Il semble mal a l'aise avec le sujet

**Question 3 - Developpement des talents**
"Comment faites-vous monter en competences les membres de votre equipe aujourd'hui ? Donnez-moi un exemple concret de quelqu'un que vous avez aide a progresser."

Bons signaux :
- Plan de developpement individualise
- Delegue des responsabilites progressivement
- Peut nommer une personne et decrire sa progression

### Phase 3 - Process & Roadmap (10 min)

Objectif : evaluer sa capacite a structurer et a collaborer avec le product.

**Question 4 - Collaboration produit**
"Comment fonctionne la collaboration entre votre equipe et le product management chez Datadog ? Quel est votre role dans la priorisation ?"

Ecouter : est-ce qu'il est un acteur ou un executant de la roadmap ?

**Question 5 - Process**
"Quand vous etes arrive chez Datadog, quels process avez-vous mis en place ou changes ? Pourquoi ? Qu'est-ce qui a marche et qu'est-ce qui n'a pas marche ?"

Bons signaux :
- Il a diagnostique avant d'agir
- Il a itere sur ses process
- Il mentionne le feedback de l'equipe

### Phase 4 - Transition & Projection (10 min)

Objectif : valider la motivation et l'adequation avec votre contexte.

**Question 6 - Le virage**
"Ce poste est un role d'Engineering Manager a plein temps. Vous ne serez plus dans le code au quotidien. Qu'est-ce qui vous excite et qu'est-ce qui vous inquiete dans cette transition ?"

Bons signaux :
- Il en est conscient et l'a deja reflechi
- Il identifie des risques reels (isolement technique, syndrome de l'imposteur, difficulte a mesurer son impact)
- Il a un plan pour rester connecte a la technique sans coder

Mauvais signaux :
- "Je continuerai a coder le soir" ou "je garderai 20% de mon temps pour coder"
- Il minimise le changement

**Question 7 - Scenario d'onboarding**
"Imaginez que vous arrivez le jour 1. Vous avez 8 devs, 2 tech leads, et un product manager. Quelles sont vos 3 priorites pour les 30 premiers jours ?"

Bons signaux :
- Ecouter / observer avant d'agir
- 1:1 avec chaque membre de l'equipe
- Comprendre la roadmap et les enjeux produit
- Ne pas tout changer d'emblee

### Phase 5 - Questions du candidat (5 min)

Laisser le candidat poser ses questions. Les questions qu'il pose en disent autant que ses reponses :

Bons signaux :
- Il demande comment le succes sera mesure
- Il demande la dynamique actuelle de l'equipe
- Il demande les defis actuels

Mauvais signaux :
- Il ne pose que des questions sur la stack technique
- Il demande s'il pourra coder

---

## 5. Grille de scoring post-entretien

| Dimension | Poids | Note /5 | Commentaire |
|-----------|-------|---------|-------------|
| Motivation pour le people management | 25% | _ | Veut-il vraiment manager ? |
| Experience de feedback/perf management | 25% | _ | A-t-il deja eu des conversations difficiles ? |
| Capacite a structurer des process | 15% | _ | Sait-il diagnostiquer et iterer ? |
| Collaboration produit | 15% | _ | Acteur ou executant de la roadmap ? |
| Projection dans le role | 10% | _ | Vision realiste de la transition ? |
| Communication / clarte | 10% | _ | Capable de synthetiser et convaincre ? |

**Seuil de passage** : note ponderee >= 3.5/5 ET aucune dimension critique (motivation, perf management) en dessous de 3/5.

---

## 6. Decision framework

### GO si :
- Il donne des exemples concrets de feedback difficile donne
- Il a une vision claire de ce que signifie "ne plus coder"
- Il pose des questions sur l'equipe, pas sur la stack
- Il decrit une approche structuree pour le perf management, meme s'il ne l'a jamais fait formellement

### NO GO si :
- Il n'a jamais eu de conversation de feedback difficile et ne semble pas pret a en avoir
- Il veut "garder du temps pour coder" comme condition
- Il est vague sur la gestion de la sous-performance
- Il se projette comme un "super tech lead" plutot que comme un manager

### MAYBE (2eme entretien necessaire) si :
- La motivation semble bonne mais les exemples manquent de profondeur
- Il est lucide sur ses lacunes et a un plan pour les combler
- Il a besoin de coaching initial (acceptable si les fondamentaux sont la)

---

## 7. Red flags a surveiller pendant le call

- **Evitement** : il change de sujet quand on parle de conflits ou de sous-performance
- **Hero syndrome** : il resolait tous les problemes lui-meme au lieu de developper son equipe
- **Manque de recul** : il ne mentionne jamais ses erreurs ou ses apprentissages
- **Motivation extrinsèque** : il veut le titre, pas le role
- **Datadog nostalgia** : s'il passe plus de temps a parler de ce qu'il fait chez Datadog qu'a se projeter chez vous

---

## 8. Questions de suivi si le call se passe bien

Pour un eventuel 2eme entretien ou pour les references :

- Demander a parler a son manager actuel ou precedent (avec son accord)
- Proposer un cas pratique : "Voici une situation reelle (anonymisee) de notre equipe. Comment la gererez-vous ?" (utiliser le cas du dev en difficulte)
- Faire rencontrer les 2 tech leads pour evaluer la dynamique

---

*Rapport genere le 2026-04-01 -- Analyse basee sur les informations fournies par le hiring manager.*
