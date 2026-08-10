# Formation_Trading_Paris

Site vitrine de Cameo Expert, centre de formation en trading — **formation-trading-paris.fr**

Site statique (HTML + CSS, JavaScript réduit au minimum) inspiré de cameo-expert.fr,
avec une identité visuelle retravaillée et une structure optimisée pour le référencement.

## Lancer le site

Aucun outil n'est nécessaire : ouvrez `index.html` dans un navigateur.
Pour un rendu identique à la production (chemins absolus, `robots.txt`, `sitemap.xml`) :

```bash
python -m http.server 8000
# puis http://localhost:8000
```

## Structure

```
index.html                            Accueil
formations.html                       Catalogue
formation-cameo-pro-access.html       Formation présentiel (2 990 €)
formation-cameo-flex-online.html      Formation en ligne / hybride (2 990 €)
formation-cameo-masterclass.html      Coaching & mentorat (250 €/mois, 6 ou 12 mois)
formation-cameo-club.html             Communauté (75 €/mois)
formation-webinaire-psychologie.html  Webinaire 1 h — psychologie du trader
guide-trading-gratuit.html            Lead magnet « guide complet du trading PDF »
pedagogie.html                        Vision pédagogique + biographie du formateur
salle-des-marches.html                Salle physique / virtuelle, accès, séminaires
faq.html                              ~26 questions, balisage FAQPage
contact.html                          Coordonnées + formulaire
mentions-legales.html                 Mentions, RGPD, cookies, CGV, risques
sitemap.xml · robots.txt

assets/css/style.css                  Design system complet (tokens, composants)
assets/js/main.js                     ~20 lignes : apparition au scroll + fermeture du menu
assets/img/                           Visuels récupérés sur le site source
_source/                              Gabarit + fragments de pages (voir ci-dessous)
```

## Modifier le site

Deux possibilités.

**A. Éditer directement les `.html` à la racine.** C'est du HTML pur, sans dépendance.
Inconvénient : l'en-tête et le pied de page sont répétés dans chaque fichier.

**B. Passer par `_source/` (recommandé pour les changements globaux).**

- `_source/template.html` — en-tête, navigation, pied de page, `<head>` commun.
- `_source/pages/<slug>.html` — le contenu propre à chaque page, précédé d'un bloc
  `<!--meta { ... } -->` contenant titre, description, mots-clés, image Open Graph,
  onglet de navigation actif et éventuel JSON-LD.

Puis régénérer :

```bash
python _source/build.py
```

Le dossier `_source/` n'a pas besoin d'être déployé (il est exclu dans `robots.txt`).

## Ce qui reste à faire avant mise en ligne

1. **Mentions légales** — compléter les champs entre crochets dans `mentions-legales.html`
   (raison sociale, SIRET, numéro de déclaration d'activité, hébergeur, adresse complète).
2. **Formulaires** — `contact.html` et `guide-trading-gratuit.html` ont `action="#"`.
   Les brancher sur un service d'envoi (Formspree, Brevo, script PHP…) ou sur le CRM existant.
3. **Guide PDF** — produire le fichier et le lier depuis `guide-trading-gratuit.html`.
4. **Prise de rendez-vous** — remplacer les liens `contact.html` par l'URL réelle de
   réservation visio si elle existe (Google Calendar / Calendly).
5. **Tarifs** — vérifier les montants affichés, repris de la grille publique du site source.
6. **Témoignages** — seul celui de Michel Ditrigano provient du site d'origine ; les deux
   autres sont des exemples à remplacer par de vrais avis avant publication.
7. **Domaine** — les `<link rel="canonical">` et le `sitemap.xml` pointent vers
   `https://formation-trading-paris.fr/` ; adapter si le domaine diffère.

## Notes techniques

- **JavaScript** : uniquement `assets/js/main.js` (~20 lignes) pour l'apparition au défilement
  et la fermeture du menu mobile. Le menu burger et les accordéons FAQ fonctionnent sans JS
  (respectivement case à cocher CSS et `<details>/<summary>` natifs) : le site reste
  entièrement utilisable JavaScript désactivé.
- **Bandeau de cotations** (accueil uniquement) : widget *Ticker Tape* de TradingView, le même
  service que celui utilisé par le site d'origine. C'est un script externe chargé en `async` —
  la seule dépendance tierce du site. Les symboles se modifient dans le bloc JSON de
  `_source/pages/index.html` (section `.ticker`). Si le script est bloqué, la hauteur du bandeau
  reste réservée (`.ticker__widget { min-height: 78px }`) : pas de saut de mise en page.
  Pour supprimer toute dépendance externe, il faudrait remplacer le widget par un défilement
  CSS avec des valeurs statiques — donc des cours figés, ce qui est déconseillé sur un site de
  formation au trading.
- **Accessibilité** : lien d'évitement, `aria-current` sur la navigation, contrastes AA,
  focus visible, `prefers-reduced-motion` respecté.
- **Polices** : Manrope et Instrument Serif via Google Fonts, avec repli sur les polices
  système si le réseau est indisponible.
