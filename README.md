# word_reduce
Create catchy brand names!

## Usage

Easy - remove vowels and repeats:

    In: word_reduce('library.tv')
    Out: 'lbry.tv'
    
You can also ask for vowels:

    In: word_reduce('Flicker', vowel=1)
    Out: 'Flickr'
    
Repeats work the same (it removes vowels and then count repeats):

    In: word_reduce('library', vowel=1, repeat=1)
    Out: 'librry'
    
Get a list of names when you have no ideas:

    In: word_reduce('Awesome',listAll=True)
    Out: {'Awesm', 'Awesom', 'Awesome', 'Awsm', 'wsm'}
    
    In: word_reduce('Natural',listAll=True)
    Out: {'Natrl', 'Natural', 'Naturl', 'Ntrl'}
    
    
